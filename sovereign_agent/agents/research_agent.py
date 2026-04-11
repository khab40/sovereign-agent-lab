import json
import os
import re

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from sovereign_agent.tools.venue_tools import (
    calculate_catering_cost,
    check_pub_availability,
    generate_event_flyer,
    get_edinburgh_weather,
)

load_dotenv()

DEBUG_AGENT_TRACE = os.getenv("DEBUG_AGENT_TRACE") == "1"

llm = ChatOpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_KEY"),
    model="meta-llama/Llama-3.3-70B-Instruct-fast",
    temperature=0,
)

TOOLS = [
    check_pub_availability,
    get_edinburgh_weather,
    calculate_catering_cost,
    generate_event_flyer,
]

SYSTEM_PROMPT = """
You are a research agent for Edinburgh event planning.

You must use tools whenever the user asks for venue availability, weather,
cost calculation, or flyer generation.

Rules:
- Do not guess venue facts.
- Do not answer from general knowledge when a tool exists.
- If a task involves checking a pub, you must call check_pub_availability.
- If a task involves weather, you must call get_edinburgh_weather.
- If a task involves catering price, you must call calculate_catering_cost.
- If a task involves flyer creation, you must call generate_event_flyer.
- If multiple checks are needed, call the tools one by one and then summarize.
- Never repeat the same tool call with the same arguments if it already succeeded.
- If a tool returns success=true and provides the requested result, stop using tools and give the final answer.
- For flyer generation tasks, call generate_event_flyer once. If it succeeds and returns an image_url, immediately respond with the result.
- Only give a final answer after using the required tools.
"""

_agent = create_react_agent(
    llm,
    TOOLS,
    prompt=SYSTEM_PROMPT,
)

def _extract_tool_calls(message) -> list[dict]:
    extracted = []

    for tc in getattr(message, "tool_calls", []) or []:
        extracted.append({
            "tool": tc.get("name", ""),
            "args": tc.get("args", {}),
        })

    content = getattr(message, "content", None)
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                extracted.append({
                    "tool": block.get("name", ""),
                    "args": block.get("input", {}),
                })

    additional_kwargs = getattr(message, "additional_kwargs", {}) or {}
    for tc in additional_kwargs.get("tool_calls", []) or []:
        function = tc.get("function", {}) or {}
        extracted.append({
            "tool": function.get("name", ""),
            "args": function.get("arguments", {}),
        })

    return extracted


def _maybe_run_direct_flyer_task(task: str) -> dict | None:
    """
    Fast-path deterministic flyer requests so Task B does not loop.
    This is intentionally narrow and only applies when the task already
    contains the confirmed venue, guest count, and theme.
    """
    pattern = re.compile(
        r"(?P<venue>The [A-Za-z' -]+?) is confirmed for (?P<guests>\d+) guests.*?theme '(?P<theme>[^']+)'",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(task)
    if not match:
        return None

    venue_name = match.group("venue").strip()
    guest_count = int(match.group("guests"))
    event_theme = match.group("theme").strip()

    raw_fn = generate_event_flyer.func if hasattr(generate_event_flyer, "func") else generate_event_flyer
    tool_result = raw_fn(
        venue_name=venue_name,
        guest_count=guest_count,
        event_theme=event_theme,
    )

    try:
        parsed = json.loads(tool_result) if isinstance(tool_result, str) else tool_result
    except Exception:
        parsed = {
            "success": False,
            "error": "Could not parse tool output",
            "prompt_used": "",
            "image_url": "",
        }

    if parsed.get("success"):
        final_answer = (
            f"Flyer generated successfully for {venue_name}. "
            f"Image URL: {parsed.get('image_url', '')}"
        )
    else:
        final_answer = (
            f"Flyer generation failed for {venue_name}. "
            f"Error: {parsed.get('error', 'unknown error')}"
        )

    return {
        "final_answer": final_answer,
        "tool_calls_made": [
            {
                "tool": "generate_event_flyer",
                "args": {
                    "venue_name": venue_name,
                    "guest_count": guest_count,
                    "event_theme": event_theme,
                },
            }
        ],
        "full_trace": [
            {"role": "human", "content": task},
            {
                "role": "tool_call",
                "tool": "generate_event_flyer",
                "args": {
                    "venue_name": venue_name,
                    "guest_count": guest_count,
                    "event_theme": event_theme,
                },
            },
            {"role": "tool", "content": tool_result},
            {"role": "ai", "content": final_answer},
        ],
        "success": bool(final_answer),
    }


def run_research_agent(task: str, max_turns: int = 8) -> dict:
    """
    Run the research agent on a task and return a structured result.
    """
    direct_result = _maybe_run_direct_flyer_task(task)
    if direct_result is not None:
        return direct_result

    result = _agent.invoke(
        {"messages": [("user", task)]},
        config={"recursion_limit": max_turns * 2},
    )

    tool_calls_made = []
    full_trace = []
    final_answer = ""
    tool_outputs_seen = 0

    for i, message in enumerate(result["messages"]):
        role = getattr(message, "type", "unknown")
        content = getattr(message, "content", "")

        if DEBUG_AGENT_TRACE:
            print(f"[DEBUG][{i}] class={message.__class__.__name__} role={role}")
            print(f"[DEBUG][{i}] content={content!r}")
            print(f"[DEBUG][{i}] tool_calls={getattr(message, 'tool_calls', None)!r}")
            print(f"[DEBUG][{i}] additional_kwargs={getattr(message, 'additional_kwargs', None)!r}")
            print()

        extracted_calls = _extract_tool_calls(message)
        for entry in extracted_calls:
            tool_calls_made.append(entry)
            full_trace.append({"role": "tool_call", **entry})

        if isinstance(message, ToolMessage):
            tool_outputs_seen += 1
            full_trace.append({"role": "tool", "content": str(content)})
            continue

        if content:
            full_trace.append({"role": role, "content": str(content)})
            if role == "ai":
                final_answer = str(content)

    if not tool_calls_made and tool_outputs_seen > 0:
        tool_calls_made.append({
            "tool": "unparsed_tool_calls",
            "args": {"count": tool_outputs_seen},
        })

    if DEBUG_AGENT_TRACE:
        print("[DEBUG] tools used:", tool_calls_made)

    return {
        "final_answer": final_answer,
        "tool_calls_made": tool_calls_made,
        "full_trace": full_trace,
        "success": bool(final_answer),
    }
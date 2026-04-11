"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = "Spent some decent time to return the list of tools used. First, LangChain packages with create_react_agent are deprecated in the source code of the original task definition. Second, made System Prompt to instruct LLM to use Tools if they are available. Thirdly, implemented proper error handling for tool calls. It started to work and returned the list of tools used "   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-fee14575-6fea-4820-8668-f6d9895fdd7c_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
After the tool result showed that The Bow Bar had capacity 80, status full, and meets_all_constraints false, the agent changed course and checked The Haymarket Vaults instead, which then returned meets_all_constraints true.
"""

SCENARIO_1_FALLBACK_VENUE = "Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Unfortunately, none of the known venues meet the capacity and dietary requirements for your event. The Albanach, The Haymarket Vaults, and The Guilford Arms have capacities of 180, 160, and 200 respectively, which are less than the required capacity of 300. The Bow Bar has a capacity of 80 and is also fully booked. Therefore, it is not possible to find a suitable venue from the known venues that can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "Your input is lacking necessary details. Please provide more information or specify the task you need help with."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
This would not be fully acceptable in a real booking assistant. The response is generic and does not clearly explain that train times are outside the assistants scope. A better response would explicitly say that the assistant only handles booking-related venue tasks and cannot help with rail travel information.
"""""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
* LangGraph graph: simple outer structure, complex behavior hidden inside the loop
* Rasa flow: larger explicit structure, behavior defined up front
* LangGraph is better for open-ended research
* Rasa is better for controlled confirmation workflows where every step should be visible and enforced
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
AMOUNT OF DEBUGGING AND FIXES, I had to do. To make the agent work with the tools, I had to rewrite the System Prompt multiple times, add error handling for tool calls, and even then it took a few tries to get it right. It was surprising how much effort was needed just to get the agent to use the tools correctly.
3 times calling flyer generation tool, created additional function to extract tool calls from the message content, and finally got it working. I also had to add a rule in the System Prompt to prevent the agent from calling the same tool with the same arguments multiple times, which was a common issue during testing.
"""
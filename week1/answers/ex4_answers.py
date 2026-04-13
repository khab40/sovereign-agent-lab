"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "The best match is 'The Albanach' at 2 Hunter Square, Edinburgh."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changing The Albanach from available to full in mcp_venue_server.py changed Query 1 automatically.
Before the change, search_venues returned both The Albanach and The Haymarket Vaults, and the agent selected The Albanach.
After the change, search_venues returned only The Haymarket Vaults, so the final answer switched to that venue.
Query 2 did not change because no venue can hold 300 vegan guests in both version.
I only updated the shared MCP server data file; the LangGraph client in exercise4_mcp_client.py did not need logic
changes for the experiment itself.
MCP improved global consistency: one server-side data change affected clients without duplicating logic. The failure risk: if the server contract changes, multiple clients can break at once.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 265   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives a stable tool interface that multiple clients can reuse, not just cleaner file organization.
The LangGraph agent and a future Rasa action can both call the same venue server without duplicating tool logic.
When the venue data changes, the client behavior changes automatically through the shared protocol, so we update one server instead of rewriting each agent.
MCP buys a shared contract, tool discovery, reuse across agents, and clearer ownership of tool behavior. The tradeoff is more moving parts than a local function.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
Planner proposes, executor acts through constrained tools, Rasa handles human confirmation, MCP owns shared tool contracts, observability catches loops/failures/cost spikes.
In details:
- The Headless Automator in `sovereign_agent/` handles open-ended research and planning because it can break a task into steps, call tools, and continue autonomously without a human guiding every turn.
- The shared MCP server in `sovereign_agent/tools/mcp_venue_server.py` exposes common tools through one interface so both the LangGraph agent and the Rasa side can use the same capabilities without duplicating tool logic.
- A planner and executor split is added in Week 3 so one component can reason about the overall strategy while another faster component performs the concrete tool calls and execution work.
- The memory layer in `sovereign_agent/memory/` stores persistent notes and retrieval data so the system can remember previous searches, bookings, and useful facts across sessions instead of starting from zero every time.
- The Rasa Digital Employee in `exercise3_rasa/` handles structured conversations with people because confirmation calls need explicit flows, predictable fallbacks, and deterministic business rule enforcement.
- The voice pipeline adds Whisper STT, Rasa CALM, an LLM, and TTS so a human caller can speak naturally while the system still routes the request through controlled conversational logic.
- Observability and safety guardrails are part of the Week 5 production system so the final agent can be monitored, audited, and kept within acceptable cost and behaviour limits during live use.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
Research - the one using LangGraph. For the call - Rasa-based.
In Exercise 2 runs, LangGraph worked well for open-ended tool use: it checked venues, handled an unavailable venue, calculated catering, checked weather, and generated a flyer.
That kind of flexible planning fits research.
In Exercise 3, Rasa was better for the call because it followed an explicit booking flow, collected guest count, vegan count, and deposit, then applied deterministic Python guards.
Swapping them looks incorrect because LangGraph is too open-ended for a high-stakes confirmation call, while Rasa is too constrained for broad autonomous research.
Research needs flexible planning, while calls need predictable contracts, bounded scope, and deterministic escalation rules.
"""

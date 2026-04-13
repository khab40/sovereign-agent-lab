# Changelog

## 2026-04-13 - Strengthened Week 1 answer analysis

- Updated the Week 1 exercise answer files to better explain failure modes,
  design rationale, local versus global correctness, trade-offs, anomalies, and
  architecture boundaries.
- Expanded the Exercise 1 prompt-formatting reflection to call out tie-breaking
  behavior, shallow distractor failure risk, and the limits of drawing global
  conclusions from a single successful run.
- Expanded the Exercise 2 LangGraph reflections to discuss safe refusal,
  out-of-scope behavior, tool-loop cost/latency risk, and the difference
  between visible graph structure and behavior hidden inside the agent loop.
- Expanded the Exercise 3 Rasa CALM reflections to cover boundary enforcement,
  cutoff-guard test gaps, probabilistic slot extraction, and the operational
  value of auditable flows.
- Expanded the Exercise 4 MCP reflections to describe shared-contract benefits,
  multi-client consistency, server-contract breakage risk, and planner/executor
  safety boundaries.
- Fixed the `LagGraph` typo in the Exercise 4 guiding-question answer and
  cleaned trailing whitespace in the updated answer files.

## 2026-03-31 to 2026-04-11 - Troubleshooting non-running tasks and failing tests

This entry summarizes the troubleshooting sequence reconstructed from the local
Git history, generated result files, and the notes captured in `docs/`.

### 2026-03-31 - Baseline setup before active run debugging

- Created the initial project structure with the Week 1 exercises, grading
  helpers, Makefile targets, Rasa exercise files, LangGraph research-agent
  scaffold, shared venue tools, MCP venue server, smoke test, and README files.
- Added `.env.example` and later expanded it so required local environment
  variables and Nebius/Rasa settings are visible without committing secrets.
- Migrated the Rasa exercise toward the Rasa Pro CALM structure by adding
  `exercise3_rasa/data/flows.yml`, updating `domain.yml`, `config.yml`,
  `endpoints.yml`, `exercise3_rasa/pyproject.toml`, `Makefile`, and the
  Exercise 3 answer template.
- Removed the old Rasa `nlu.yml` and `rules.yml` files after moving the
  exercise toward CALM flows and `from_llm` slot extraction.
- Updated `week1/exercise2_langgraph.py` and `week1/grade.py` to match the
  revised exercise expectations.
- Added root and Rasa-specific `uv.lock` files so the student environments are
  reproducible during test and task execution.
- Refined the README and `.gitignore` over several follow-up commits to document
  setup, execution, and environment expectations.

### 2026-04-09 - Initial `make test` failure before exercise work

- After the first setup pass, ran the baseline verification sequence:
  `make install`, `make smoke`, then `make test`.
- The initial `make test` run failed before the exercise work was completed.
  The tracked checklist records this as `Run make test - failure!`.
- The failure was expected at that stage because
  `sovereign_agent/tools/venue_tools.py` still had the placeholder
  `generate_event_flyer` implementation, and
  `sovereign_agent/tests/test_week1.py` contains a guard test that fails while
  the flyer tool returns a `STUB` error.
- The fix was to implement `generate_event_flyer` instead of changing the test:
  add the OpenAI-compatible Nebius image client, build a prompt from venue,
  guest count, and theme, call `black-forest-labs/flux-schnell`, and return
  structured JSON with `success`, `prompt_used`, and `image_url`.
- Re-ran `make test` after the flyer implementation as part of Exercise 2 and
  continued with the remaining task and grading checks.

### 2026-04-09 - Rasa CALM task execution and configuration fixes

- Ran the Exercise 3 Rasa CALM chat flows and captured terminal logs for the
  happy path, high-deposit escalation path, and out-of-scope request path in
  `docs/notes-logs-records.md`.
- Updated `exercise3_rasa/endpoints.yml` so the Nebius-hosted LLM and embedding
  models are configured through the OpenAI-compatible provider format:
  `provider: openai`, `openai/meta-llama/Llama-3.3-70B-Instruct`, and
  `openai/Qwen/Qwen3-Embedding-8B`.
- Documented the Rasa endpoint/provider configuration in `README.md` so repeated
  LiteLLM provider-list output points users back to the expected
  OpenAI-compatible Nebius model-group settings.
- Enabled the Exercise 3 cutoff guard in `exercise3_rasa/actions/actions.py`.
  The action now escalates once the current time is past 16:45 so confirmations
  cannot proceed too close to the 5 PM deadline.
- Verified the Rasa behavior with server and chat-client runs, including a
  temporary forced-true cutoff-condition test, then documented the results in
  `week1/answers/ex3_answers.py`.
- Documented that CALM uses `from_llm` slot extraction for values such as guest
  count and vegan count, so the old Rasa `FormValidationAction` parsing class
  was not needed.

### 2026-04-09 to 2026-04-11 - Dependency and LangGraph compatibility fixes

- Updated `pyproject.toml` to use current pinned LangChain and LangGraph
  packages that work with the exercise code:
  `langchain==1.2.15`, `langchain-openai==1.1.12`,
  `langchain-core==1.2.27`, and `langgraph==1.1.6`.
- Regenerated `uv.lock` after the dependency changes so the project has a
  reproducible environment for the repaired exercise runs.

### 2026-04-09 to 2026-04-11 - Exercise 2 LangGraph agent troubleshooting

- Reworked `sovereign_agent/agents/research_agent.py` so the agent actually
  uses the available venue, weather, catering, and flyer tools instead of
  answering from general knowledge.
- Added a system prompt that explicitly requires tool use for venue checks,
  weather checks, catering-price calculation, and flyer generation.
- Added `DEBUG_AGENT_TRACE` support to print message classes, roles, content,
  tool calls, and provider-specific message metadata while debugging.
- Added robust tool-call extraction across the message shapes encountered during
  testing: `message.tool_calls`, list-based `tool_use` content blocks, and
  `additional_kwargs["tool_calls"]`.
- Added `ToolMessage` trace handling so tool outputs are preserved in
  `full_trace`, and added a fallback `unparsed_tool_calls` marker when tool
  outputs exist but a provider-specific tool-call shape cannot be parsed.
- Added a narrow deterministic fast path for confirmed flyer-generation tasks.
  This prevents the LLM loop from repeatedly calling `generate_event_flyer` with
  the same arguments and lets Task B return a structured result directly.
- Updated the research-agent model to
  `meta-llama/Llama-3.3-70B-Instruct-fast` during the final troubleshooting pass.
- Generated and saved the Exercise 2 outputs in `week1/outputs/ex2_results.json`
  and filled in `week1/answers/ex2_answers.py` with the observed tool calls,
  final answers, and debugging notes.

### 2026-04-09 to 2026-04-11 - Flyer tool implementation

- Replaced the `generate_event_flyer` stub in
  `sovereign_agent/tools/venue_tools.py` with a real Nebius OpenAI-compatible
  image-generation call using `black-forest-labs/flux-schnell`.
- Added support for both `venue_name` and `pub_name` arguments so the tool can
  tolerate the argument names produced by different agent runs.
- Returned consistent JSON for both success and failure, including
  `success`, `prompt_used`, `image_url`, and `error` where relevant.
- Moved the OpenAI image client construction inside the `try` block, set a
  `timeout=120.0`, and disabled retries with `max_retries=0` so timeout
  failures are caught and returned as structured tool output.
- Refreshed `week1/outputs/ex2_results.json` after the final flyer-tool and
  model changes. The final recorded Task B run shows a handled image-generation
  timeout rather than an uncaught crash.

### 2026-04-09 to 2026-04-11 - Exercise 4 MCP client troubleshooting

- Investigated initial Exercise 4 runs where the output did not provide useful
  evidence because tool calls were not being surfaced clearly.
- Added an MCP-specific system prompt in `week1/exercise4_mcp_client.py` that
  instructs the agent to use `search_venues`, then fetch details for the best
  match with `get_venue_details` when the user asks for an address.
- Added dynamic Pydantic argument-model construction from MCP input schemas so
  discovered MCP tools are exposed to LangChain as structured tools with usable
  argument schemas.
- Updated MCP trace extraction to capture `message.tool_calls`,
  `additional_kwargs["tool_calls"]`, list-style `tool_use` blocks, and
  `ToolMessage` outputs.
- Ran the required Exercise 4 experiment by temporarily changing The Albanach's
  availability in the MCP venue server, observing the agent switch to The
  Haymarket Vaults, and then reverting the temporary data change.
- Saved Exercise 4 results in `week1/outputs/ex4_results.json` and documented
  the experiment in `week1/answers/ex4_answers.py`.

### 2026-04-09 to 2026-04-11 - Exercise answer and result artifacts

- Filled in `week1/answers/ex1_answers.py` with the observed prompt-formatting
  results for the large and small model runs.
- Filled in `week1/answers/ex2_answers.py` with tool-call order, venue choice,
  catering cost, weather result, flyer prompt/result, fallback behavior,
  impossible-constraint behavior, out-of-scope behavior, Mermaid output, and
  reflection notes.
- Filled in `week1/answers/ex3_answers.py` with the Rasa conversation traces,
  high-deposit escalation, out-of-scope CALM behavior, cutoff-guard test notes,
  and CALM-vs-old-Rasa reflection.
- Filled in `week1/answers/ex4_answers.py` with MCP tool discovery results,
  venue-query results, the required experiment write-up, MCP-vs-hardcoded
  comparison, and Week 5 architecture notes.
- Added generated result snapshots:
  `week1/outputs/ex1_results.json`, `week1/outputs/ex2_results.json`, and
  `week1/outputs/ex4_results.json`.

### 2026-04-09 to 2026-04-11 - Supporting documentation

- Added troubleshooting and run logs in `docs/notes-logs-records.md`.
- Added a Week 1 submission checklist in `docs/week1-submission-checklist.md`.
- Added architecture notes and Mermaid/UML-style diagrams:
  `docs/architecture/agent-use-cases-uml.md`,
  `docs/architecture/week1-assignment-snake.md`, and
  `docs/architecture/week5-voice-flow-uml.md`.

### 2026-04-11 - Final cleanup commit

- Clarified the Exercise 3 action-file comments to say the old Rasa approach
  used an old form-validation subclass, avoiding the misleading implication that
  a `FormValidationAction` class is still needed in the CALM implementation.
- Switched the Exercise 2 research agent to the fast Llama 3.3 70B Nebius model.
- Hardened flyer generation by catching client construction and request timeout
  failures inside `generate_event_flyer`.
- Refreshed the Exercise 2 output JSON with the latest weather and flyer-tool
  run results.

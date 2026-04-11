# Agent Use Cases (Mermaid-Compatible)

Mermaid does not support native UML `usecaseDiagram` syntax, so this file uses
a `flowchart` to represent the same actors, system boundaries, and use cases.

This diagram places the two bots as separate system boundaries:

- `Headless Automator` = `sovereign_agent/`
- `Rasa Digital Employee` = `exercise3_rasa/`

The human users are outside those boundaries as actors.

```mermaid
flowchart LR

Operator["Human User<br/>(automator owner)"]
Caller["Human Caller<br/>(pub manager)"]
Trigger["External Trigger<br/>(WhatsApp / file watch / API)"]
MCP["Shared MCP Tool Server"]

subgraph HA["Headless Automator<br/>sovereign_agent/"]
direction TB
HA1(["Submit autonomous task"])
HA2(["Plan research workflow"])
HA3(["Call venue and web tools"])
HA4(["Produce summary or recommendation"])
HA5(["Store reusable results"])
end

subgraph RA["Rasa Digital Employee<br/>exercise3_rasa/"]
direction TB
RA1(["Start booking confirmation"])
RA2(["Collect booking details"])
RA3(["Validate business rules"])
RA4(["Confirm booking or escalate"])
RA5(["Answer only in-scope requests"])
end

Operator --> HA1
Trigger --> HA1
HA1 --> HA2
HA2 --> HA3
HA3 --> HA4
HA4 --> HA5
MCP --> HA3

Caller --> RA1
RA1 --> RA2
RA2 --> RA3
RA3 --> RA4
Caller --> RA5
MCP --> RA3
```

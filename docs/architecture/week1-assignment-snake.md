# Week 1 Assignment Path

```mermaid
flowchart LR

subgraph R1[ ]
direction LR
A1[Start: Fork repo] --> A2[Clone fork] --> A3[Create .env] --> A4[Add NEBIUS_KEY] --> A5[Add RASA_PRO_LICENSE] --> A6[Run make install] --> A7[Run make smoke] --> A8[Run make test]
end

A8 --> B8

subgraph R2[ ]
direction RL
B8[Run make ex1] --> B7[Check ex1_results.json] --> B6[Fill week1/answers/ex1_answers.py] --> B5[Run make grade-ex1]
end

B5 --> C5

subgraph R3[ ]
direction LR
C5[Run make ex2-a] --> C6[Implement generate_event_flyer<br/>in sovereign_agent/tools/venue_tools.py] --> C7[Run make test] --> C8[Run make ex2-b / ex2-c / ex2-d] --> C9[Check ex2_results.json] --> C10[Fill week1/answers/ex2_answers.py] --> C11[Run make grade-ex2]
end

C11 --> D11

subgraph R4[ ]
direction RL
D11[Run make install-rasa] --> D10[Run make ex3-train] --> D9[Terminal 1: make ex3-actions] --> D8[Terminal 2: make ex3-chat] --> D7[Run 3 required conversations] --> D6[Paste traces into ex3_answers.py] --> D5[Uncomment cutoff guard in actions.py] --> D4[Run make ex3-retrain] --> D3[Restart action server] --> D2[Rerun chat and test cutoff guard] --> D1[Run make grade-ex3]
end

D1 --> E1

subgraph R5[ ]
direction LR
E1[Run make ex4] --> E2[Check ex4_results.json] --> E3[Change The Albanach to full<br/>in mcp_venue_server.py] --> E4[Rerun make ex4] --> E5[Observe changed result] --> E6[Revert MCP change] --> E7[Fill week1/answers/ex4_answers.py] --> E8[Run make grade-ex4]
end

E8 --> F8

subgraph R6[ ]
direction RL
F8[Run make grade] --> F7[Run make check-submit] --> F6[Confirm output JSON files] --> F5[Confirm answer files are filled] --> F4[Confirm flyer tool is implemented] --> F3[Confirm cutoff guard is uncommented] --> F2[Push fork] --> F1[Submit fork URL]
end

## Self-Improving AI Agent – VE.AI Assignment

### Agent Description
This project implements a task assistant agent that answers math questions requiring calculation.

### Tools
- Calculator tool (required for correct execution)

### Early Mistakes
- Agent answers without using the calculator
- Produces answers too early

### Evaluation
Each run is evaluated using rule-based checks:
- Was the calculator used?
- Was the answer produced too early?
- Was the tool output respected?

### Learning Mechanism
Mistakes are logged in persistent memory.
Repeated mistakes trigger new behavioral rules.
Example: After repeatedly skipping the calculator, the agent learns to always use it first.

### Demonstration
Early runs show incorrect behavior.
Later runs show improved accuracy and correct tool usage.

### Limitations
- Rule-based learning only
- No complex reasoning or reinforcement learning
- Designed for clarity, not intelligence


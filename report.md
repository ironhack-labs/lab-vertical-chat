### Overview
This lab explored building a vertical domain conversational agent (“OrderBot”) using OpenAI’s chat completions API and Panel for interactivity.  
The objective was to simulate a food ordering assistant capable of maintaining conversational context, clarifying details, and summarizing structured orders.


### What I Did
- Implemented an interactive conversation loop using Panel widgets and an OpenAI chat context.
- Designed and tested three prompt engineering versions:
  - **Version 1:** Structured conversational flow with strict phases (questioning → summary → confirmation).
  - **Version 2:** Few-shot guided prompt for more natural and human-like responses.
  - **Version 3:** Guardrailed version with a JSON schema handoff for potential POS integration.
- Evaluated the performance of each version across coherence, accuracy, and adherence to constraints.


### Key Findings
- **Version 1** provided a predictable structure but sometimes stalled at greetings without progressing to order collection.
- **Version 2** showed a friendlier tone and more fluid conversation, but occasionally produced off-menu confusion (e.g., “frankfurt not on menu”).
- **Version 3** handled contextual dialogue best and produced structured, machine-readable output (JSON) once the order was confirmed.


### Errors / Hallucinations
- Model occasionally denied menu items that existed (hallucinated “not on menu”).
- In rare cases, skipped summarization when the user gave multiple details at once.
- With loose temperature settings, it occasionally invented menu extras (e.g., “hot dog”).
- No syntax errors or malformed JSON in Version 3.


### What I Learned
- Explicit menu grounding and role instructions are essential to prevent hallucination.
- Few-shot examples drastically improve conversational flow and style.
- Schema-based prompting(Version 3) is highly effective for structured outputs and downstream system integration.
- Temperature tuning significantly influences conversational creativity vs. reliability.
- Clear phase control and constraints yield more predictable, production-ready behavior.


### Next Steps
- Integrate real-time order validation from a database or API.
- Add a context reset button for multi-order sessions.
- Expand JSON schema for delivery, tax, and payment details.
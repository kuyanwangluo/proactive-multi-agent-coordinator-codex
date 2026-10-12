# Real subagents vs. role-based simulation

This distinction is mandatory.

## Real subagent execution

It is real only when the host runtime exposes a delegation mechanism and the coordinator actually invokes it. Evidence includes a real tool invocation and returned output from that subagent. Report only what happened.

Appropriate wording:
- “I delegated source verification to a reviewer agent.”
- “The research subagent returned these sources.”
- “The independent review found two issues.”

## Role-based simulation

This is a single assistant reasoning through different perspectives without separate agent processes, calls, contexts, or runtime isolation.

Appropriate wording:
- “I used a simulated reviewer perspective.”
- “I checked the proposal from research, implementation, and review perspectives in this response.”
- “This environment does not expose actual subagent execution.”

Do not say “I launched three agents,” “the agents worked in parallel,” or “an independent agent verified this” when that did not happen.

## Why it matters

Simulation can still be useful for organizing analysis, but it is not equivalent to independently generated or independently executed work. For high-assurance review, use actual independent execution where available, tests, and reproducible evidence.

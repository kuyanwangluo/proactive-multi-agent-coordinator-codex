# Orchestration protocol

## 1. Plan work packages

Create a task plan only when delegation is useful. Use stable IDs such as `R1`, `P1`, `I1`, and `V1`.

Each work package should contain:
- `id`
- `role`
- `objective`
- `dependencies`
- `inputs`
- `scope`
- `out_of_scope`
- `deliverable`
- `acceptance_criteria`
- `risk_level`
- `execution_mode` (`actual_subagent` or `role_simulation`)
- `status`

## 2. Choose execution mode honestly

### Actual subagent execution

Use only if the current Codex/runtime provides a real subagent, agent tool, or documented delegation mechanism. Invoke it using the available interface, provide the handoff, and wait for its result. Do not invent tool names or assume that a tool exists.

For independent research/review, ask agents to work independently before sharing other agents' conclusions when possible. For file edits, define ownership of files to avoid conflicting writes. Prefer one implementer and a separate reviewer rather than multiple agents editing the same files.

### Role-based simulation

If no actual delegation interface is available, carry out specialist analyses sequentially in the current context. Label them as simulated roles, not separate agents. Do not claim parallel execution, separate model calls, independent runtime isolation, or actual delegation.

## 3. Dependency and scheduling rules

- Start independent work packages in parallel only when the runtime supports it.
- Run prerequisite work before dependent tasks.
- Use the smallest number of specialists that covers the actual need.
- Set a concrete expected output for every package.
- Avoid having two workers modify the same files concurrently unless the runtime provides safe conflict management.
- If blocked, identify the missing input and ask the user only if they can resolve it.
- Re-plan when requirements change; preserve completed work that remains valid.

## 4. Handoff lifecycle

`pending -> in_progress -> completed`

Alternative transitions:
- `pending -> blocked`
- `in_progress -> blocked`
- `in_progress -> rejected` (does not meet criteria)
- `blocked -> pending` after unblock
- `rejected -> in_progress` after a revised handoff

A work package is not `completed` merely because a response was returned. Check its deliverable against acceptance criteria.

## 5. Integration and conflict resolution

Create a synthesis table with:
- Work package / role
- Status
- Deliverable
- Evidence or tests
- Assumptions
- Open issues
- Acceptance result

Resolve contradictions in this order:
1. Re-check the requirement brief.
2. Inspect source evidence or reproduce the test.
3. Ask for focused follow-up if needed.
4. Explain unresolved disagreement to the user if it affects the decision.

Never use majority vote as a substitute for evidence. Do not hide material uncertainty.

## 6. Suggested scheduling patterns

### Research + independent review
1. Researcher gathers evidence and sources.
2. Reviewer checks source quality and missing counterarguments independently.
3. Coordinator synthesizes and flags unresolved claims.

### Plan + implement + review
1. Planner creates plan and acceptance tests.
2. User confirms any material trade-off or scope decision.
3. Implementer produces the artifact.
4. Reviewer checks it against the approved plan.
5. Coordinator reports test results and remaining gaps.

### Multi-option strategy
1. Two or three specialists independently propose viable approaches if the runtime supports it.
2. Coordinator compares cost, quality, risk, time, and reversibility.
3. User chooses a direction.
4. Only then proceed with the chosen implementation.

Do not run every pattern for every task.

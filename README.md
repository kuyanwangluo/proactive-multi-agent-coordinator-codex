# Proactive Multi-Agent Coordinator — Codex Skill

A deployment-oriented Codex Skill for proactive requirements discovery, option-based decisions, specialist task orchestration, handoff contracts, explicit approval gates, and result verification.

## Package contents

```text
proactive-multi-agent-coordinator/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── orchestration-protocol.md
│   ├── real-vs-simulated.md
│   └── approval-policy.md
├── templates/
│   ├── handoff-template.md
│   └── requirement-brief.md
├── tests/
│   └── test-cases.md
└── scripts/
    └── validate_skill.py
```

## Install for your user account

### macOS / Linux

From the extracted package directory:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R proactive-multi-agent-coordinator "$HOME/.agents/skills/"
python3 "$HOME/.agents/skills/proactive-multi-agent-coordinator/scripts/validate_skill.py"
```

Codex skill discovery paths can vary by version/configuration. The current Codex documentation lists `$HOME/.agents/skills` as a user-level location; some versions/guides also use `$HOME/.codex/skills`. If your Codex installation does not discover it, copy the folder to:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R proactive-multi-agent-coordinator "$HOME/.codex/skills/"
```

If you already have a folder with this name, back it up or merge intentionally rather than overwriting it.

### Windows PowerShell

After extracting the ZIP, from the directory containing `proactive-multi-agent-coordinator`:

```powershell
$dest = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item -Recurse ".\proactive-multi-agent-coordinator" $dest
python "$dest\proactive-multi-agent-coordinator\scripts\validate_skill.py"
```

If your Codex version uses `$HOME\.codex\skills`, copy the skill folder there instead.

## Invoke it

In Codex, use the skill explicitly in a prompt:

```text
$proactive-multi-agent-coordinator Help me plan and execute this project. Ask me about important trade-offs, then coordinate specialist work where available.
```

You can also open `/skills` in supported Codex interfaces to inspect available skills. If the skill does not appear after installation, restart or reload Codex and check the path.

## Project-local installation

For a repository-specific skill, place the folder under:

```text
<repository>/.agents/skills/proactive-multi-agent-coordinator/
```

This allows the skill to live with the project and be version-controlled for teammates.

## Real multi-agent execution: important limitation

This skill specifies orchestration behavior; it does not itself create or enable subagents. The coordinator must use an actual delegation tool provided by the current Codex/runtime to perform real subagent work. Tool availability differs by runtime and configuration.

If no delegation tool is available, the skill requires the coordinator to use **role-based simulation** and explicitly say so. It must not claim separate agents ran, worked in parallel, or independently verified results.

For robust real multi-agent execution, configure your Codex/runtime with the supported agent delegation mechanism and permissions. Keep handoffs explicit, assign file ownership, and use a separate reviewer where possible.

## Approval behavior

The skill requires explicit confirmation before consequential external actions such as sending, publishing, purchases, destructive changes, disclosure of sensitive information, or security/access changes. It can still draft, plan, inspect, and prepare a preview before approval.

## Validate package structure

Run:

```bash
python3 scripts/validate_skill.py
```

On Windows:

```powershell
python scripts/validate_skill.py
```

This checks the package structure and basic frontmatter constraints. It does not test Codex runtime discovery or guarantee behavioral compliance.

## Behavioral tests

See `tests/test-cases.md` for 12 acceptance scenarios covering ambiguity, delegation, simulated roles, approval gates, prompt injection, conflicts, and sensitive data handling.

## Documentation

Codex Skills use a folder containing a required `SKILL.md` with YAML frontmatter and optional supporting files. Refer to the current official documentation for version-specific installation and runtime behavior:
- https://developers.openai.com/codex/skills

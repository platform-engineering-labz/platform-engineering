# Knowledge and project content standards

Use this guide to keep a large platform engineering monorepo navigable and avoid duplicate research or implementations.

## Decide where content belongs

- **`engineering-reference/guides/`**: concepts, how a technology works, tradeoffs and official sources.
- **`engineering-reference/examples/`**: short, focused teaching examples that accompany guides.
- **`engineering-reference/troubleshooting/`**: errors, diagnostic commands, root causes and remediation.
- **`engineering-reference/architecture/`**: design alternatives, diagrams and decisions.
- **`labs/`**: runnable integrated scenarios involving several components.
- **`modules/`**: reusable infrastructure components shared across labs.
- **`tooling/`**: container images, scripts, local/devcontainer tooling and validation.
- **`.agents/skills/`**: task-specific AI guidance; **`AGENTS.md`** is the repository-wide policy.

Search existing content across *all* these locations before creating new material. If the same concept already has a canonical guide, update it and link to the implementation instead of duplicating explanations.

## Suggested metadata for substantial Markdown guides

```yaml
---
title: Example: GitLab Runner isolation on EKS
topics: [gitlab, kubernetes, eks, network-security, iam]
status: draft
last-reviewed: YYYY-MM-DD
related:
  - labs/gitlab-runners-on-eks/
  - engineering-reference/guides/kubernetes/
---
```

Replace the placeholders, omit non-existent `related` links, and set `last-reviewed` only after an actual review. This metadata is descriptive and not yet indexed automatically.

## Suggested sections

1. **Question / objective:** What problem is being explored?
2. **Short answer:** Current conclusion with known caveats.
3. **Implementation / example:** Synthetic, reusable code where appropriate.
4. **Verification:** What was actually tested, with commands and results; clearly label anything untested.
5. **Tradeoffs / security:** Alternatives, limitations, blast radius.
6. **References:** Direct links to primary authoritative sources and version/date context.
7. **Related content:** Links to canonical guides, existing labs, or reusable modules.

When updating an existing page, replace outdated information or append genuinely new findings. Keep the history in Git; do not paste full chat transcripts. All published content must be safe for a public repository.

# Agent instructions — Platform Engineering Monorepo

This public repository is the **source of truth for committed professional platform-engineering work**: executable code, reusable modules, scripts, infrastructure examples, labs, architecture, troubleshooting, technical explanations, and curated references. It is not a chat transcript archive. Use `main` as the authoritative reference.

## Select the appropriate workflow

- **Ordinary technical question:** Answer normally. Do not automatically inspect or modify GitHub.
- **Asked to review/search/compare earlier repository work:** Read [repository-knowledge-review](.agents/skills/repository-knowledge-review/SKILL.md). Search **the whole repository**, including executable code and documentation. Report what already exists, related improvements, or whether a new project/topic is appropriate. This is **read-only** unless the user explicitly requests a change.
- **Explicitly asked to create, enhance, save, update, append, commit, publish, or "Add this to my repository":** Read [knowledge-curation](.agents/skills/knowledge-curation/SKILL.md). Inspect existing implementations and documentation before choosing whether to extend, refactor, or add new content.
- Do not claim to remember prior chats unless their relevant contents are available in the current conversation or committed files.

## Monorepo organization

- **Functional projects and code:** Keep self-contained projects, Terraform modules, scripts, manifests, pipelines, tests, and other executable artifacts in suitably named directories. Reuse existing project paths when relevant; create new top-level directories only when the content warrants them.
- **Explanations and learning references:** Use `engineering-reference/` for guides, small educational examples, architecture, troubleshooting, and curated links. Maintain [the topic index](engineering-reference/INDEX.md) when its material changes.
- **Related content:** Link explanations to implementations and related topics. Avoid redundant copies, near-duplicate examples, unnecessary subdirectories, and raw conversation dumps.
- Keep runnable code complete where practical; include usage, validation, limitations, and authoritative sources where relevant. Do not claim tests were run unless they actually were.
- This is a **public** repository. Use public documentation and independently generated, synthetic examples only. Never publish employer-proprietary code or internal architecture, accounts, identifiers, secrets, sensitive logs, or personal information.
- Inspect actual files, rather than trusting an index or prior answer to represent current contents.

## GitHub changes

- **Only with explicit authorization to save/update:** Branch from `main`, edit the appropriate files, commit on that branch, verify commit and changed paths through GitHub, and open a PR targeting `main`.
- Return the direct PR URL and commit SHA. **Never automatically merge into `main`.**
- Never force-push, delete repositories, or change branch protections without explicit approval. Do not require the user to run Git commands or use Codespaces.
- If GitHub access is missing or a step fails, report it; never claim success without verification.

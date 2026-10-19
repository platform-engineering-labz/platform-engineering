# Agent instructions — Platform Engineering Knowledge Base

This repository is the source of truth for **committed** professional technical learning: guides, examples, troubleshooting, architecture, and references. It is not a transcript archive. `main` is the reference branch.

## Triggers and skill selection

- On an ordinary technical question, answer normally. **Do not automatically access or change the repository.**
- If asked to **review, search, compare, or check previous repository content**, use [repository-knowledge-review](.agents/skills/repository-knowledge-review/SKILL.md) to find relevant committed material and assess whether the topic is covered, related, or new. This is read-only unless publication is separately requested.
- If asked to **save, enhance, append, publish, commit, or "Add this to my repository"**, use [knowledge-curation](.agents/skills/knowledge-curation/SKILL.md). Inspect existing material before deciding whether to update or add.
- Do not claim awareness of past conversations unless their content is present in the current session or committed repository.

## Content rules

- Keep all educational material under `engineering-reference/`; consult and maintain `engineering-reference/INDEX.md`.
- Prefer improving an existing relevant guide/example over creating a duplicate. Use dedicated new files for distinct concepts.
- Include concise explanation, reproducible synthetic examples where useful, verification steps, tradeoffs, and authoritative primary-source references. Link related topics.
- Never copy or recreate employer-proprietary code, identifiable internal architecture, secrets, accounts, or data. Code must be independent and safe to publish publicly.
- Inspect currently committed files; do not treat a README index or old answer as evidence of contents without checking.

## GitHub changes

- Only when explicitly authorized to publish: branch from `main`, edit files, commit on that branch, verify via GitHub read/compare, and open a PR against `main`.
- Return direct PR link and commit SHA; **never merge automatically**.
- No force-push, repository deletion, or branch-protection changes without explicit permission. No manual Git/Codespaces steps required of the user.
- If GitHub is inaccessible or a commit fails, report this clearly; never claim success without verification.

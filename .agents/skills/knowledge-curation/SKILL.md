---
name: knowledge-curation
description: Use when the user explicitly requests saving a technical explanation or example, updating existing committed knowledge, adding content to the repository, or creating a GitHub pull request. Favor consolidating related topics over duplicating guides.
---

# Curate and publish technical learning

1. Read root `AGENTS.md` and `engineering-reference/INDEX.md` on `main`. Find and read relevant committed files before deciding what to change.
2. Choose **revise** for improved explanations, **append** for genuinely additive information in the same topic, or **new topic** when materially distinct. Avoid transcript dumps, repeated questions, and duplicate files.
3. Organize under `engineering-reference/`: `guides/{aws,kubernetes,terraform,gitlab}/` for concepts; `examples/` for reproducible labs; `troubleshooting/` for diagnostics; `architecture/` for designs; `references/` for curated sources. Make new subdirectories if warranted.
4. Each contribution should preserve the core question, concise answer, explanation, realistic *synthetic* example where applicable, validation approach, limitations/tradeoffs, date-sensitive caveats, and primary-source references. Link related guides/examples instead of copying them.
5. Update `engineering-reference/INDEX.md` for newly added or materially changed topics. Check links and formatting; run tests or static checks where possible.
6. For explicitly requested publication, create a descriptive feature branch from `main`, commit only approved-scope changes, verify the files and commit via GitHub, then open a PR targeting `main`. Return the PR link, commit SHA, and brief summary. Do not merge.
7. Never put proprietary employer code, details, identifiers, screenshots, secrets, or chat-personal data in the public repository. State when verification could not be performed.

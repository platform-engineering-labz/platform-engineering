---
name: knowledge-curation
description: Use for explicitly requested edits or publication in the platform engineering monorepo, including working code, labs, modules, configuration, technical guides, architecture, and references. Reuse and improve existing projects where practical.
---

# Build, maintain, and publish repository content

1. Read `AGENTS.md` on `main` and inspect related **existing files throughout the repository**. Use `engineering-reference/INDEX.md` as a map for documentation, not a replacement for searching.
2. Decide whether to **extend/refactor existing code**, **revise/append related documentation**, or **add a new self-contained project/topic**. Avoid duplicate code, overlapping explanations, and chat transcript dumps.
3. Put runnable projects and substantial code in an appropriate existing or new project directory; small explanatory samples, guides, architecture, troubleshooting, and source references belong under `engineering-reference/`. Link related code and reference material.
4. Include practical installation/usage, configuration assumptions, validation or tests where warranted, security implications, tradeoffs, and primary-source references. Prefer synthetic, generic examples. Never claim unperformed tests succeeded.
5. Update relevant indexes, entrypoint README files, internal links, and tests as needed. Preserve unrelated existing content.
6. **Only after explicit publication request:** Create a descriptive feature branch from `main`; commit changes, verify file paths and commit through GitHub, and open a PR targeting `main`. Report its URL, full commit SHA, and what was/wasn't tested. **Do not merge.**
7. Never publish proprietary employer details, secrets, real internal accounts/hostnames, personal details, or private data in this public repository. Report failed or unavailable GitHub operations transparently.

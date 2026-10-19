---
name: knowledge-curation
description: Use when the user explicitly asks to save, update, or publish runnable platform engineering code, modules, tools, guides, labs, or research in the GitHub monorepo. Reuse existing content and maintain cross-topic navigation.
---

# Maintain and publish monorepo content

1. Read root `AGENTS.md`, the [content standards](../../../engineering-reference/references/content-standards.md), and existing relevant files **throughout the repository**. `engineering-reference/INDEX.md` is a map, not proof of existing material.
2. Decide: **reuse/refactor existing code**, **revise or append a canonical document**, or **create a truly new project/topic**. Avoid transcript dumps, duplicates and unneeded directories.
3. Put runnable integrated scenarios under `labs/`, shared infrastructure modules under `modules/`, development helpers and images under `tooling/`, and educational guides/examples/architecture/troubleshooting under `engineering-reference/`. Link documentation to implementations rather than cloning the same code.
4. For significant content, include objective/question, implementation, setup, validation, tradeoffs/security, official sources and related topics. Use multi-topic tags when useful; identify untested examples honestly. Never publish employer-proprietary or personal material.
5. Update appropriate READMEs, links, `engineering-reference/INDEX.md`, and tests/validation as warranted. Avoid claims that roadmap entries are functional implementations.
6. On explicit publication request, create a descriptive branch from `main`, commit the changes, verify SHA and file diff through GitHub, and open a PR to `main`. Return the direct PR URL and SHA. Never merge automatically or force-push.
7. Preserve unrelated files; report verification failures or unavailable access clearly. No need for the user to run Git commands or use Codespaces.

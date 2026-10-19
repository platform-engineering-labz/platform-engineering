---
name: repository-knowledge-review
description: Read-only review of existing committed platform engineering code, projects, labs, guides, and references when the user explicitly asks to compare a question or task against repository content.
---

# Review existing repository work (read-only)

1. Read `AGENTS.md` on `main` and consult `engineering-reference/INDEX.md` for reference content.
2. Search **the entire repository**, not only documentation. Inspect real code, project READMEs, labs, modules, manifests, scripts, architectures, and guides related to the user's question.
3. Classify the request as **already covered**, **related (enhance/extend existing work)**, or **new**. Give exact relevant paths, similarities, gaps, and any conflicting or outdated implementations.
4. Answer the user's technical question and recommend whether to revise existing code/docs, append related information, or add a separate project/topic; use current authoritative sources if appropriate.
5. Do not create files, branches, commits, or PRs unless the user explicitly asks to make changes.
6. Do not infer previous private conversations from a filename; only cite context actually available in the current session or committed files.

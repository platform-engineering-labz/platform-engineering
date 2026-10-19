# Documentation standards

Use progressive disclosure: **[root glossary](../../README.md) → [topic index](../INDEX.md) → topic README → details.md → implementation**.

| Level | File | Content |
| --- | --- | --- |
| 1 | Root `README.md` | Alphabetical, one-line glossary with links; no lengthy explanations |
| 2 | Topic `README.md` | Problem, concise answer, 3–5 impact-ranked recommendations, next links |
| 3 | Topic `details.md` | Deeper analysis, tradeoffs, validation and authoritative sources |
| 4 | `labs/`, `modules/`, `tooling/` | Runnable code, usage, dependencies and verified tests |

For a new topic, search the **entire repository** first. Enhance the canonical guide instead of creating duplicates. Use relative Markdown links, descriptive link text and cross-links between related subjects. Never link to nonexistent implementations as if they were completed.

Keep recommendations in a compact table with priority (`P0` critical, `P1` high, `P2` medium), action and reason. Distinguish **verified**, **proposed**, and **unknown** claims. Cite primary documentation and note time/version sensitivity. Avoid irrelevant conversation drift, private infrastructure, secrets and employer material.

Place detailed code examples in reusable implementation folders rather than inflating overviews. Update the root glossary and topic index whenever a new canonical topic is published.

## Optional website

Markdown must remain readable in GitHub and compatible with MkDocs. A future MkDocs Material site can provide full-text search, navigation and glossary browsing; deploy via GitHub Pages or GitLab Pages only after the publishing workflow is explicitly selected. Do not assume a site is live.

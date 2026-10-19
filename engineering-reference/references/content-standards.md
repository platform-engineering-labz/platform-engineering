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

## Ebook illustration policy

Use a **topic-specific PNG** where a visual clarifies architecture, data flow, trust boundaries, state transitions or operational decision-making. Place `diagram.png` next to the chapter or topic README that embeds it, with descriptive alt text. Link to a deeper technical guide rather than treating the picture as the implementation. Prefer one meaningful diagram to decorative screenshots or duplicated generic illustrations. Do not add images to empty placeholders or directories that have no substantive content.

Review every diagram against the associated analysis: distinguish desired from actual state, permissions from isolation, and compatibility from EOL. Keep labels legible at ebook width, preserve the explanatory text for search/accessibility, and verify that every image link resolves. If a visual repeats an existing guide diagram in a chapter introduction, keep the copies synchronized when the underlying explanation changes.

### Diagram production standard

The authoritative editable source is a **local `diagram.mmd`** beside the README; `diagram.png` is a generated artifact, not hand-drawn decoration. Use professional architecture conventions: named system boundaries, explicit flow direction, distinguish control plane from data plane, meaningful edge labels, consistent neutral palette, readable type and accurate trust boundaries. Diagrams must match the text and be specific to their folder. Do not copy one generic PNG into multiple unrelated topics. The GitHub Actions [diagram renderer](../../.github/workflows/diagrams.yml) uses [Mermaid configuration](../../tooling/diagrams/mermaid-config.json) to regenerate all PNGs when source diagrams change. A diagram must not be treated as validated until the renderer succeeds.

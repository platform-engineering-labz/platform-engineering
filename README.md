# Platform Engineering

A public monorepo for independently developed cloud and platform engineering **labs, reusable code, tools, architectures and technical knowledge**. Work is organized by executable scenario or reusable component, with cross-linked explanations.

## Repository map

| Location | Purpose |
| --- | --- |
| [Engineering reference](engineering-reference/INDEX.md) | Guides, troubleshooting, small examples, architecture and primary sources |
| [Labs](labs/) | Runnable, multi-technology implementations and experiments |
| [Modules](modules/) | Reusable building blocks (starting with Terraform) |
| [Tooling](tooling/) | Container images, scripts, development containers and validation |
| [AGENTS.md](AGENTS.md) and [.agents/skills/](.agents/skills/) | Persistent instructions for AI assistants |

Start with the [content standards](engineering-reference/references/content-standards.md) when publishing new topics. Proposed lab subjects are listed in [labs/README.md](labs/README.md); **they are not implemented yet**.

## Restore the ChatGPT workflow

In your **existing Platform Engineering ChatGPT Project**, put these instructions in Project settings, or paste them into a new chat:

```text
Use platform-engineering-labz/platform-engineering as the source of truth for my committed platform-engineering code, labs, architecture, and technical knowledge.

Answer normal questions without accessing GitHub. When I request repository review, read AGENTS.md and relevant .agents/skills/, search the entire repository, and tell me what already exists, what can be enhanced, and what is new. Do not edit anything for a read-only review.

When I say "Add this to my repository" or explicitly request changes, inspect existing work first, then update/refactor related files or create a properly organized project or guide. Use labs/ for integrated runnable scenarios, modules/ for reusable code, tooling/ for development assets, and engineering-reference/ for explanations. Keep indexes and cross-links current.

For writes, branch from main, commit and verify, then open a PR targeting main. Return the PR link and SHA. Never merge, force-push, delete repositories, or alter branch protection without explicit authorization. No manual Git or Codespaces steps. Publish only generic, independently generated material, never employer code, private infrastructure or secrets.
```

Only content actually committed to GitHub persists across sessions. [GitHub integration walkthrough](engineering-reference/references/github-integration-workflow.md).

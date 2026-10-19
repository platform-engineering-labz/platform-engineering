# Platform Engineering

A public platform-engineering monorepo for independent projects, working labs, reusable code, architectures, troubleshooting, and technical reference material.

- [Engineering reference and topic index](engineering-reference/INDEX.md)
- [Repository-wide AI instructions](AGENTS.md)
- [Reusable agent skills](.agents/skills/)

## Restore the ChatGPT workflow

In your **existing Platform Engineering ChatGPT Project**, add these instructions to its Project settings, or paste them into a new chat when needed:

```text
Use platform-engineering-labz/platform-engineering as my source of truth for committed platform-engineering projects, code, labs, architecture, and professional knowledge.

For ordinary questions, answer normally. When I ask you to review the repository, use GitHub to read AGENTS.md and relevant .agents/skills/ files, then search existing code and documentation. Tell me what is covered, what can be enhanced, or what is new. Repository reviews are read-only unless I also request changes.

When I say "Add this to my repository" or explicitly request saving/updating something, inspect existing work first. Improve or append related code/docs where appropriate, otherwise create a new well-organized project or topic. Place working code in a suitable project/module directory and learning references under engineering-reference/. Update indexes and links when relevant.

For writes, branch from main, commit and verify changes, open a PR targeting main, and give me the PR URL and commit SHA. Never auto-merge, force-push, delete repositories, or change branch protections. Do not require manual Git commands or Codespaces. Use public or independently generated examples; never employer-proprietary details or secrets.
```

Only committed content is persisted in GitHub; unrelated previous chats are not automatically present. [GitHub integration walkthrough](engineering-reference/references/github-integration-workflow.md).

# Platform Engineering

Public, independent technical learning and a reusable professional knowledge base.

Start with the [Engineering Reference index](engineering-reference/INDEX.md). The repository's [AGENTS.md](AGENTS.md) defines the persistent workflow and its [skills](.agents/skills/) handle repository review and knowledge curation.

## Restore the workflow in a new ChatGPT conversation

Connect the GitHub integration and paste this prompt (or save it as ChatGPT Project instructions):

```text
My professional technical knowledge source of truth is platform-engineering-labz/platform-engineering (main). When I ask you to review the repository, read AGENTS.md and the applicable .agents/skills/ instructions. Search relevant committed examples, then tell me whether this question is already covered, related to an existing topic that should be enhanced, or new. Answer the question; don't edit the repository just because I asked for a review.

Only when I explicitly say "Add this to my repository" or request saving/updating content: improve an existing topic or create a new one under engineering-reference/, maintain the index, create a descriptive branch from main, commit and verify changes, and open a PR targeting main. Provide its URL and commit SHA. Never merge, force-push, or change protections. Use public or synthetic examples only; no employer code, private details, or secrets. Do not require manual Git commands or Codespaces.
```

Previous technical discussions are only in this knowledge base when explicitly committed. [Archived GitHub integration walkthrough](engineering-reference/references/github-integration-workflow.md).

# Platform Engineering

Public educational labs and reference materials for AWS, Kubernetes, Terraform, GitLab, and related platform engineering topics.

Browse the [engineering-reference](engineering-reference/) directory for guides, examples, troubleshooting, architecture, and references.

## Restore ChatGPT GitHub workflow

If the ChatGPT instructions or GitHub connection are lost, reconnect GitHub in **ChatGPT → Settings → Plugins**, then copy and paste this entire prompt into a new chat:

```text
When I say "Add this to my repository", use my connected GitHub integration and the repository platform-engineering-labz/platform-engineering.

1. Create a descriptive feature branch from main.
2. Add or update the requested files. Default to engineering-reference/ for learning content.
3. Commit to the feature branch and verify the commit and changed files.
4. Open a pull request targeting main. Return the PR link and commit SHA.

Never merge into main automatically. Do not force-push, delete repositories, or change branch protections without explicit approval. No routine confirmation requests, manual Git commands, or Codespaces steps. If GitHub access is unavailable, say so rather than claiming success. Use public or synthetic learning examples only; no employer code, secrets, or private infrastructure details.
```

Your changes should always go through a feature branch and pull request. **You review and merge the PR yourself.**

For the earlier connection test and detailed setup, see [GitHub integration walkthrough](engineering-reference/references/github-integration-workflow.md).

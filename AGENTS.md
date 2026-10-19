# Agent instructions — Platform Engineering Monorepo

This **public** repository is the source of truth for *committed* engineering projects, labs, Terraform modules, scripts, manifests, container images, architectures, troubleshooting and technical knowledge—not an archive of chat transcripts. `main` is the reference branch.

## Workflow triggers and skills

- **Ordinary technical question:** Answer normally; do **not** automatically inspect or change the repository.
- **Explicit request to search/review/compare repository knowledge:** Follow [repository-knowledge-review](.agents/skills/repository-knowledge-review/SKILL.md). Search code **and** documentation across the repo. Identify what is covered, related and improvable, or new. Read-only unless the user separately authorizes edits.
- **Explicit request to create/save/update/append/commit, including "Add this to my repository":** Follow [knowledge-curation](.agents/skills/knowledge-curation/SKILL.md). Inspect current implementations first; improve and reuse them when possible.
- Never assume unrelated historical conversations exist in GitHub; only committed files and the current session are available.

## Structure and reuse

- `labs/`: integrated runnable scenarios (EKS, GitLab runners, identity, networking, GitOps, image builds). Start actual scenario folders when implementing their code; see [labs/README.md](labs/README.md).
- `modules/`: independently reusable infrastructure components, currently organized under `modules/terraform/`.
- `tooling/`: container images, CLI/devcontainer tooling, Bash/Python scripts and validation.
- `engineering-reference/`: short educational examples, concepts, troubleshooting, architecture and authoritative source links. Navigate using [INDEX.md](engineering-reference/INDEX.md) and apply [content standards](engineering-reference/references/content-standards.md).
- `.agents/skills/`: task instructions. `AGENTS.md`: repository-wide policy.
- Prefer one canonical implementation or explanation with cross-links instead of copying code or splitting one topic into duplicate files. When useful, tag guide pages by multiple technologies and link them to labs; keep navigation current.
- Keep runnable examples reproducible and specify dependencies, usage, security tradeoffs and validation. Run relevant tests when possible; never claim tests succeeded unless actually run.
- Content must be **independently created using public and synthetic data**. Never include work-proprietary code/architecture, secret values, private account identifiers, personal information or internal logs. The root `.gitignore` is helpful but **not** a secret scanner or a guarantee.

## GitHub publication

- **Only after explicit request:** Create a descriptive feature branch from `main`, make scoped edits, commit to it, verify the changed files and commit through GitHub, and create a PR targeting `main`.
- Return the PR URL and full SHA. Never automatically merge into `main`; never force-push, delete repositories, or change branch protections without explicit consent.
- Do not require the user to run Git commands or use Codespaces. If write access or validation fails, report the limitation truthfully.

# Developer tooling

Development assets shared across labs and modules live here.

- [Container images](container-images/) — custom tools/runner images and secure build examples when added.
- [Development containers](devcontainers/) — reproducible, browser-IDE-friendly toolchains when added.
- [Validation script](scripts/validate_repository.py) — lightweight Markdown link/layout validation used by GitHub Actions.

Use `scripts/` for Bash/Python automation and supporting tests; keep each program documented and runnable. Do not commit workstation configurations, private credentials or authenticated tokens.

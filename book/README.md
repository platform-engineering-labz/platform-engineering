# Reading the handbook

This is a **technical book with two reading modes**:

1. **Read in order:** Foundations → Infrastructure → CI/CD → GitOps → Security → Operations → Practice. Each part introduces the concepts needed by later chapters.
2. **Find an answer:** use the [glossary](../README.md), [topic index](../engineering-reference/INDEX.md), or the website's built-in **Search**. A topic overview leads to ranked recommendations and then detailed analysis.

The book is intentionally honest about its maturity: only four research topics are published as chapters so far. Other parts are editorial introductions and roadmaps, **not** claims that the underlying guides or labs exist.

## Table of contents

| Part | Core questions | Current reading |
| --- | --- | --- |
| [I. Foundations](01-foundations/README.md) | What do containers, Kubernetes and networking provide? | Conceptual roadmap |
| [II. AWS and Infrastructure](02-infrastructure/README.md) | How are EKS and infrastructure upgraded safely? | EKS rollback |
| [III. Containers and CI/CD](03-cicd/README.md) | How should GitLab jobs build and publish images? | Buildah / ECR |
| [IV. GitOps and Deployment](04-gitops/README.md) | How do Flux and Helm declare and reconcile desired state? | GitOps context |
| [V. Security](05-security/README.md) | How do we contain privileged workloads? | Runner isolation |
| [VI. Operations](06-operations/README.md) | How do we discover unsupported dependencies? | EOL inventory |
| [VII. Practice](07-practice/README.md) | How do we turn guidance into tested implementations? | Lab and tooling catalog |

**Editorial rule:** chapter introductions explain *why* the topic matters; linked topic `README.md` files summarize the problem and recommendations; `details.md` provides depth and primary sources; implementation files live in `labs/`, `modules/` and `tooling/`.

[← Glossary](../README.md) · [Reference index](../engineering-reference/INDEX.md)

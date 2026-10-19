# Platform Engineering Knowledge Base

A concise, linked glossary of platform-engineering concepts, research and reusable implementations. **Start with a term, open its topic overview, then follow links to deeper analysis, primary sources or working code.** Only published material is linked as a completed guide.

## Glossary

| Term | What it means | Learn more |
| --- | --- | --- |
| **Amazon EKS** | AWS-managed Kubernetes control plane; version upgrades, add-ons and recovery need coordinated planning. | [Upgrade and rollback](engineering-reference/guides/aws/eks-upgrade-rollback/README.md) |
| **AWS ECR** | Container registry; Kubernetes pulls and CI build pushes use distinct authentication paths. | [Buildah and ECR](engineering-reference/guides/gitlab/kubernetes-runner-buildah-ecr/README.md) |
| **Buildah** | Daemonless OCI image builder, potentially usable without privileged DinD. | [Buildah on GitLab runners](engineering-reference/guides/gitlab/kubernetes-runner-buildah-ecr/README.md) |
| **Calico / Cilium** | Kubernetes networking and policy implementations; isolation depends on the installed CNI and rules. | [Privileged runner isolation](engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| **DinD** | Docker-in-Docker, often privileged in CI and therefore a significant node-isolation concern. | [Runner security](engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| **EKS managed add-ons** | AWS-distributed cluster components whose installed and compatible versions must be checked separately. | [EOL inventory](engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) |
| **End-of-life (EOL)** | A product release no longer supported under its applicable lifecycle policy. | [Lifecycle scanning](engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) |
| **Flux / GitOps** | Reconciles Kubernetes desired state from version-controlled sources. | [Flux lifecycle inventory](engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) |
| **GitLab CI Kubernetes executor** | Runs CI jobs in Kubernetes pods; permissions, identity and isolation need explicit controls. | [Build authentication](engineering-reference/guides/gitlab/kubernetes-runner-buildah-ecr/README.md) · [Isolation](engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| **Helm** | Kubernetes application packaging; chart version and deployed application version can differ. | [Helm EOL inventory](engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) |
| **IRSA** | IAM roles for Kubernetes service accounts on EKS, used for short-lived AWS workload credentials. | [Build identity](engineering-reference/guides/gitlab/kubernetes-runner-buildah-ecr/README.md) |
| **Karpenter** | Kubernetes node provisioning and lifecycle automation. | [Runner node isolation](engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| **Kyverno** | Kubernetes admission and policy engine for workload guardrails. | [Privileged workload controls](engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| **Terraform** | Declarative infrastructure provisioning; provider support can lag cloud APIs. | [EKS rollback considerations](engineering-reference/guides/aws/eks-upgrade-rollback/README.md) |

## Explore the repository

| Area | What to expect |
| --- | --- |
| [Technical reference](engineering-reference/README.md) | Topic overviews and linked in-depth guides |
| [Reference index](engineering-reference/INDEX.md) | Browse published guides by technology |
| [Labs](labs/README.md) | End-to-end runnable scenarios and proposed labs |
| [Modules](modules/) | Reusable infrastructure components |
| [Tooling](tooling/) | Scripts, container images and validation utilities |

## How to read and contribute

**Glossary → topic README → detailed guide → runnable implementation.** Topic READMEs give a brief problem statement, conclusion and ranked recommendations. Detailed analysis belongs in linked `details.md`; actual tested code belongs in `labs/`, `modules/` or `tooling/`. Avoid duplicating explanations and never publish private or employer-specific material.

For conventions, see [documentation standards](engineering-reference/references/content-standards.md). For AI-assisted updates, see [AGENTS.md](AGENTS.md) and the [GitHub workflow](engineering-reference/references/github-integration-workflow.md).

### Publishing as a website

These relative Markdown links work in GitHub and can be used by a static documentation generator such as MkDocs Material. **No site is deployed yet.** Prefer GitHub Pages for this GitHub-hosted source; GitLab Pages is an alternative if a GitLab-hosted publishing workflow is desired.

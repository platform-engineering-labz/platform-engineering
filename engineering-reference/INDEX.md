# Engineering reference index

This is the navigation hub for **committed** engineering explanations; it is not a complete inventory of past ChatGPT conversations. For executable multi-component work, see [labs](../labs/), [reusable modules](../modules/), and [tooling](../tooling/).

## Guides by technology and function

| Area | Directory | Typical scope |
| --- | --- | --- |
| AWS | [guides/aws/](guides/aws/) | EKS, VPC, IAM, EC2, ECR, storage drivers |
| Kubernetes | [guides/kubernetes/](guides/kubernetes/) | Pods, controllers, scheduling, RBAC, admission |
| Terraform | [guides/terraform/](guides/terraform/) | Providers, modules, state, environments |
| GitLab | [guides/gitlab/](guides/gitlab/) | CI/CD, runners, workspaces |
| GitOps | [guides/gitops/](guides/gitops/) | Flux, Helm, reconciliation |
| Security | [guides/security/](guides/security/) | Identity, policy, supply chain, EOL |
| Networking | [guides/networking/](guides/networking/) | Calico, Cilium, CNI, NetworkPolicy |
| Storage | [guides/storage/](guides/storage/) | CSI, EBS, EFS and persistence |
| Containers | [guides/containers/](guides/containers/) | Docker, Buildah, Podman, runtime isolation |
| Linux | [guides/linux/](guides/linux/) | System tools, Bash, Python environments |
| Observability | [guides/observability/](guides/observability/) | Diagnostics, metrics, logging, monitoring |

## Other reference formats

- [Small teaching examples](examples/)
- [Troubleshooting](troubleshooting/)
- [Architecture and design decisions](architecture/)
- [Curated references and content conventions](references/)
- [Content standards and cross-topic metadata](references/content-standards.md)

## Search and knowledge reuse

When a question crosses areas, look for both technology tags and end-to-end scenarios. For example, GitLab Runner DinD isolation may relate to Kubernetes privileged workloads, AWS workload identity, Calico networking, Karpenter and ECR registry controls.

A repository review should search **the entire repository**, not only these folders. Prefer a canonical guide plus links to runnable code. Use the [standards](references/content-standards.md) for topic tags and related paths.

## Published topic guides

| Topic | Guide |
| --- | --- |
| Privileged GitLab Runner / DinD isolation | [Security review](guides/security/privileged-gitlab-runners/README.md) |
| GitLab Kubernetes executor / Buildah / ECR | [Build and authentication review](guides/gitlab/kubernetes-runner-buildah-ecr/README.md) |
| Helm and Kubernetes dependency EOL tracking | [Lifecycle inventory review](guides/security/kubernetes-workload-eol-inventory/README.md) |
| EKS rollback and Terraform | [Upgrade recovery review](guides/aws/eks-upgrade-rollback/README.md) |

These guides summarize confirmed discussion topics, not an exhaustive audit of pinned conversations. The ChatGPT pinned-list view was not available for enumeration, and the supplied Claude share page could not be retrieved. The excluded topics **Sync Claude Skills** and **Buildah Compose Equivalent** are not included. Further guides require source discussion access and review.

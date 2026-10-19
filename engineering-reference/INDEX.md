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

None yet. Directories and scenario roadmaps are placeholders until their content is implemented and reviewed. Add links to **actual** guides/labs here as they are published.

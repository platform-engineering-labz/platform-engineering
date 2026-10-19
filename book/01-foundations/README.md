# Part I — Foundations

Platform engineering builds repeatable environments by combining operating systems, containers, orchestration, identity and networks. A container packages a process and dependencies; Kubernetes schedules and reconciles containers, but does not by itself guarantee workload isolation or lifecycle support.

## Concepts to establish

| Concept | Why it matters | Where it appears later |
| --- | --- | --- |
| Linux namespaces and capabilities | Define process boundaries and privilege | [Runner isolation](../../engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| OCI images and registries | Define build and distribution artifacts | [Buildah and ECR](../../engineering-reference/guides/gitlab/kubernetes-runner-buildah-ecr/README.md) |
| Kubernetes scheduling and networking | Define placement and communication | [Runner isolation](../../engineering-reference/guides/security/privileged-gitlab-runners/README.md) |
| Declarative configuration | Separates desired from observed state | [EOL scanning](../../engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) |

**Status:** This is a reading roadmap, not a completed foundational tutorial. Continue to [Part II — Infrastructure](../02-infrastructure/README.md).

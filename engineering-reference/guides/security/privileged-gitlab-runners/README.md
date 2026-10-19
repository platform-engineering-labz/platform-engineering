# Privileged GitLab Runner and DinD isolation

## Problem
Docker-in-Docker builds on Kubernetes may require privileged containers. A compromised build can gain capabilities unavailable to ordinary pods; namespace separation alone does not provide node isolation.

## Analysis
Privileged pods can expose the host kernel and node resources. IRSA restricts AWS API permissions, not Linux privileges. Kyverno can control admission, Calico can enforce pod network policy, and Karpenter can provision dedicated nodes, but none alone makes privileged workloads equivalent to unprivileged ones. Image pulls, CI job downloads and arbitrary build-time curl requests have different egress requirements.

## Ranked recommendations
| Rank | Impact | Recommendation | Rationale |
| --- | --- | --- | --- |
| 1 | Critical | Prefer rootless BuildKit/Buildah or another verified unprivileged build path | Removes privileged DinD requirement where feasible |
| 2 | Critical | Run privileged builds on dedicated, tainted, disposable nodes and restrict scheduling | Reduces co-tenancy and persistence after compromise; not a host-escape guarantee |
| 3 | High | Deny privileged pods by default with a narrowly scoped Kyverno exception | Prevents unrelated workloads from inheriting the exception |
| 4 | High | Apply Calico default-deny ingress/egress and explicitly allow DNS, approved registries and required services | Reduces lateral movement and uncontrolled network reachability |
| 5 | High | Scope IRSA permissions to minimum ECR actions and resources; prevent access to node credentials | Limits cloud-side blast radius |
| 6 | Medium | Separate registry traffic through approved mirrors/proxies and govern arbitrary build egress independently | Keeps required downloads possible without claiming a total internet block |
| 7 | Medium | Rotate nodes, scan images, audit exceptions and validate isolation with adversarial tests | Detects drift and limits exposure duration |

## Validation
Test a denied privileged pod outside the exception, cross-job connectivity, access to metadata/credentials, registry pull/push, proxy bypass, node placement and teardown. Do not claim parity with unprivileged pods.

## References
- [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Kubernetes NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [AWS EKS IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)

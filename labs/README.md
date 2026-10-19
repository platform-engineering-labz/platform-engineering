# Integrated platform labs

This area is for **runnable, multi-component demonstrations**, not stand-alone notes. Each lab should contain its own README, prerequisites, architecture, reproducible manifests/code, a test/validation path, teardown instructions, and security considerations. Use synthetic identifiers; never reuse work systems or configurations.

## Candidate labs (not implemented yet)

| Candidate | Technologies / questions it connects |
| --- | --- |
| `eks-platform/` | EKS, managed node groups, EC2 launch templates, Karpenter, upgrades and rollback |
| `workload-identity/` | IAM, IRSA, EKS Pod Identity, service accounts, ECR access |
| `gitlab-runners-on-eks/` | Kubernetes executor, helper containers, Docker-in-Docker, Buildah, isolation, GitLab CI |
| `gitops-flux/` | Flux, Helm, cluster add-ons, policies and continuous reconciliation |
| `network-security/` | Calico, Cilium, NetworkPolicy, admission policy, privileged workloads |
| `secure-image-builds/` | Rootless/container builds, private registries, proxying, image controls, EOL tracking |

Create an individual lab directory **when there is executable content**; do not mistake this roadmap for completed work. Put reusable building blocks in [modules](../modules/) and conceptual explanations in [engineering-reference](../engineering-reference/).

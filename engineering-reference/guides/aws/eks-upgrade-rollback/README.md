# EKS Kubernetes version rollback and Terraform

## Problem
An EKS control-plane upgrade can create compatibility or workload issues. Operators need to know whether a rollback feature can be used through Terraform.

## Analysis
AWS API capabilities and Terraform AWS provider resource support are distinct. An AWS announcement does not prove that `aws_eks_cluster` exposes a matching rollback argument or operation. Rollback eligibility, supported version transitions, time windows and effects on nodes/add-ons must be checked against current AWS and provider documentation.

## Ranked recommendations
| Rank | Impact | Recommendation | Rationale |
| --- | --- | --- | --- |
| 1 | Critical | Validate the currently supported AWS rollback API, prerequisites and constraints before upgrading | Avoids assuming recoverability |
| 2 | High | Inspect the pinned Terraform AWS provider schema and changelog for rollback support | Distinguishes provider support from AWS feature availability |
| 3 | High | Maintain a tested recovery plan for nodes, add-ons, workloads and CRDs | Control-plane rollback alone may not restore compatibility |
| 4 | Medium | Use staging upgrades and compatibility checks before production | Reduces upgrade failures |
| 5 | Medium | Document out-of-band recovery operations and reconcile Terraform state afterward | Avoids configuration drift |

## References
- [AWS EKS version rollback announcement](https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/)
- [Terraform AWS provider EKS cluster](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster)

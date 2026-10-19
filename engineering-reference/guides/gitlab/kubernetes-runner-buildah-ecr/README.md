# GitLab Kubernetes executor: Buildah and ECR

## Problem
Container builds in GitLab's Kubernetes executor need AWS ECR authentication without embedding long-lived registry credentials or unnecessarily enabling privileged Docker-in-Docker.

## Analysis
Buildah can build OCI images without a Docker daemon, but rootless operation depends on the container image, user namespaces, storage driver and cluster security settings. IRSA supplies AWS credentials to the job service account, not automatically to every arbitrary image-pull mechanism. The ECR credential helper and `aws ecr get-login-password` are different authentication approaches; validate the helper's compatibility with the chosen tool.

## Ranked recommendations
| Rank | Impact | Recommendation | Rationale |
| --- | --- | --- | --- |
| 1 | Critical | Use a dedicated least-privilege Kubernetes service account with IRSA for build jobs | Avoids static AWS keys |
| 2 | High | Prefer unprivileged Buildah after validating user namespaces and storage behavior | Reduces host exposure |
| 3 | High | Use ECR login via AWS CLI and short-lived token, or verify credential-helper integration end to end | Avoids assuming helper support |
| 4 | High | Separate Kubernetes image-pull authentication from in-job image push authentication | Different components resolve credentials |
| 5 | Medium | Pin Buildah/AWS CLI image versions and test push/pull with the actual executor | Improves reproducibility |
| 6 | Medium | Apply scoped network policies and registry endpoint access | Reduces unnecessary egress |

## Validation
Confirm the job's AWS identity, successful ECR login, image build/push, non-root permissions and denial of unrelated AWS actions. Document any environment-specific user-namespace prerequisites.

## References
- [GitLab Kubernetes executor](https://docs.gitlab.com/runner/executors/kubernetes/)
- [Amazon ECR registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html)

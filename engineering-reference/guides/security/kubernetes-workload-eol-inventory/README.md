# Kubernetes workload dependency and EOL inventory

## Problem
Helm charts and Kubernetes manifests deploy controllers, sidecars and images whose lifecycle is not fully represented by a chart version or by endoflife.date.

## Analysis
Chart version, application version, container digest, CRD version, Kubernetes API compatibility and managed add-on release are separate dimensions. An EOL catalog is useful where it has a matching product but is not a comprehensive Helm-chart database. AWS EKS CSI and secrets-store components require checking upstream release channels and AWS add-on compatibility separately.

## Ranked recommendations
| Rank | Impact | Recommendation | Rationale |
| --- | --- | --- | --- |
| 1 | Critical | Inventory rendered Helm manifests and plain YAML for every container image and digest | Captures deployed dependencies, including sidecars |
| 2 | High | Track chart, app, controller and CRD versions independently | Prevents false lifecycle assumptions |
| 3 | High | Match known software to endoflife.date and official upstream support policies | Uses authoritative evidence where available |
| 4 | High | Track EKS managed add-on versions and Kubernetes compatibility from AWS sources | Avoids relying on generic EOL mappings |
| 5 | Medium | Automate image vulnerability scanning, release monitoring and dependency alerts | Surfaces security and upgrade work |
| 6 | Medium | Label unknown lifecycle status explicitly and assign a review owner | Avoids treating missing data as supported |

## Validation
Render representative charts, extract image references, compare them with actual cluster images and record sources and last-checked dates.

## References
- [endoflife.date](https://endoflife.date/)
- [Helm template](https://helm.sh/docs/helm/helm_template/)
- [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)

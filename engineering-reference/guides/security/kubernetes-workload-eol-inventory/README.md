# EOL and support scanning for GitLab CI, Flux, Helm, Terraform and EKS

## Problem
A GitOps repository can pin apparently current Helm charts while deploying unsupported applications, images, controllers, Kubernetes APIs or EKS add-ons. A useful scanner must identify unsupported dependencies **and** disclose gaps in coverage without misclassifying chart releases as application releases.

## Analysis
Our platform-engineering discussions span EKS managed node groups and Karpenter, Terraform, GitLab Kubernetes runners, Flux, Helm, Kyverno, Calico/Cilium, ECR, CSI and secrets drivers. Scan these as separate lifecycle surfaces:

- **Git desired state:** Flux `HelmRelease` (both `spec.chart.spec` and `spec.chartRef`), `HelmRepository`, `OCIRepository`, `Kustomization`, ordinary Kubernetes YAML, Terraform EKS/add-on/module declarations, and container build definitions.
- **Resolved releases:** Helm chart version is not reliably the workload app version. Obtain chart metadata (`appVersion`), render manifests and collect all images (including init containers and sidecars); track images by digest when possible. For umbrella charts, scan every component independently.
- **Actual cluster:** Git alone cannot prove which images and versions are running. Optionally reconcile against live workloads, Flux status, installed Helm releases, EKS control-plane version, managed add-ons and node AMIs.
- **Support sources:** Use endoflife.date where a verified product/cycle mapping exists, then official upstream support/release policies, AWS EKS add-on compatibility APIs and vendor release notes. An image vulnerability scan is complementary, not proof of lifecycle support.

Do not assume every named component has a current endoflife.date product slug or that its cycle is its full semantic version. Validate mappings and API response schema before enforcement. `aws eks describe-addon-versions` reports compatible versions, **not** the currently installed add-on or its end-of-support date; use `describe-addon` for installed version and vendor documentation for support.

## Ranked recommendations

| Rank | Impact | Recommendation | Why |
| --- | --- | --- | --- |
| P0 | Critical | Separate chart, application, image, Kubernetes API, EKS add-on and node/AMI lifecycle records | Prevents false EOL assessments |
| P0 | Critical | Render Flux-managed Helm charts and inspect all resulting containers, including sidecars/init containers | Finds dependencies invisible in chart metadata |
| P0 | Critical | Inventory installed EKS add-ons and compare with `describe-addon-versions` for the target Kubernetes version | Detects compatibility issues without inventing EOL dates |
| P1 | High | Resolve `HelmRelease` chart references, OCI tags/digests, Kustomize overlays and Terraform variables/modules | Avoids missed or incorrectly parsed versions |
| P1 | High | Keep `UNMAPPED`, `UNKNOWN`, `UNPINNED`, `UNSUPPORTED`, `WARN` and `OK` distinct | Makes missing evidence visible |
| P1 | High | Fail CI only on validated unsupported/EOL findings; report uncertain cases and enforce a separate coverage threshold | Reduces false-positive pipeline failures |
| P1 | High | Preserve scanner exit status, pin dependencies and publish JSON/SARIF plus human-readable artifacts | Makes GitLab findings actionable and auditable |
| P2 | Medium | Add weekly scheduled scans and Renovate-driven version-update MRs | Shortens remediation lead time |
| P2 | Medium | Compare Git desired state with live EKS/Flux resources using read-only credentials | Finds drift and unmanaged workloads |
| P2 | Medium | Assign owners to unmapped components and periodically verify authoritative lifecycle links | Expands coverage systematically |

## Suggested implementation

Keep this as a reusable **tooling** project, not a single large Bash/Python snippet embedded in this guide. A future implementation could use:

```text
tooling/eol-scanner/
  README.md
  eol-map.yaml
  requirements.txt
  scripts/eol_scan.py
  tests/
  examples/gitlab-ci.yml
```

Mapping records should specify component type, source of the *resolved* version, product/cycle normalization, official fallback source and optional exception expiry. Avoid mapping `kube-prometheus-stack` directly to the Prometheus lifecycle: it can deploy Prometheus, Alertmanager, exporters, Grafana and more.

A safe scanner pipeline has stages for discovery, resolution, lookup, evaluation and reporting. Cache rate-limited upstream API responses; handle network errors explicitly. Compare dates only after parsing a valid lifecycle policy. Do not interpret `eol: false` as indefinite support; it means no known EOL date in that source.

### GitLab CI reliability

Use a pinned scanner image with locked dependencies and a tested entrypoint. If streaming output through `tee`, enable `set -o pipefail` in a shell that supports it, or write the report directly and propagate the scanner's status. Publish artifacts with `when: always` and set failure policy intentionally for merge requests versus scheduled audits.

### AWS checks

- `aws eks describe-cluster`: running Kubernetes version.
- `aws eks list-addons` and `aws eks describe-addon`: installed managed add-ons and versions.
- `aws eks describe-addon-versions --kubernetes-version ... --addon-name ...`: available compatible versions, not EOL proof.
- Track AWS VPC CNI, CoreDNS, kube-proxy, EBS CSI and EFS CSI where applicable; distinguish AWS-managed add-ons from self-managed Helm installations.
- Inventory Secrets Store CSI Driver and AWS Secrets Manager provider separately, since a provider's lifecycle need not match the driver's.
- For managed node groups and Karpenter, inspect AMI/OS release lifecycle independently of the control-plane version.

## Validation and acceptance criteria

1. Fixture coverage: `HelmRelease` direct chart and `chartRef`, `OCIRepository` tag/digest, Kustomize overlay, Terraform variable-based cluster version, and multiple YAML documents.
2. Chart fixture with differing chart/app versions and images for init containers and sidecars.
3. API fixtures for EOL date, `true`, `false`, unknown cycle, missing slug, timeout and malformed data.
4. EKS add-on fixture that distinguishes installed version, compatible versions and missing support dates.
5. GitLab test proves a real `FAIL` returns nonzero **even when output is piped to `tee`**.
6. Report preserves source URL, check date, version provenance, uncertainty and remediation owner.
7. Scanner does not require production cluster access for static checks; optional runtime reconciliation uses least-privilege read-only credentials.

## Scope
This is an engineering design/review tailored from the supplied Claude discussion and our platform engineering topics. It is **not** a tested implementation against a real Flux repository. The sample script's broad YAML parsing, regex Terraform parsing, chart-to-app mapping, guessed lifecycle cycles and unguarded network lookups should not be adopted without the corrections above.

## References
- [endoflife.date API](https://endoflife.date/docs/api)
- [Flux HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/)
- [Flux OCIRepository](https://fluxcd.io/flux/components/source/ocirepositories/)
- [Helm template](https://helm.sh/docs/helm/helm_template/)
- [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)
- [EKS describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html)
- [GitLab CI job artifacts](https://docs.gitlab.com/ci/jobs/job_artifacts/)

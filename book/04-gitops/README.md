# Part IV — GitOps and Deployment

Flux reconciles declared Kubernetes resources from Git and OCI sources. Helm charts simplify packaging but introduce a key distinction: **chart versions are not necessarily application versions**, and the rendered chart can introduce multiple workloads and images.

The currently published treatment is the [Flux/Helm EOL inventory overview](../../engineering-reference/guides/security/kubernetes-workload-eol-inventory/README.md) and its [technical analysis](../../engineering-reference/guides/security/kubernetes-workload-eol-inventory/details.md).

Dedicated Flux source-controller, HelmRelease, Kustomize and reconciliation chapters remain planned, not published.

[← CI/CD](../03-cicd/README.md) · [Next: Security →](../05-security/README.md)

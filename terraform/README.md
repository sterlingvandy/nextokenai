# Databricks Terraform configuration (example)

This folder contains an example Terraform configuration that configures the HashiCorp `databricks/databricks` provider.

Authentication

- The provider reads credentials from environment variables:
  - `DATABRICKS_HOST` — the Databricks workspace URL (e.g., https://<instance>.databricks.com)
  - `DATABRICKS_TOKEN` — a personal access token

Or, pass them as Terraform variables with: `-var "databricks_host=<host>" -var "databricks_token=<token>"`.

Quick start

```bash
cd terraform
# Set env variables (preferred):
export DATABRICKS_HOST="https://<your-workspace>"
export DATABRICKS_TOKEN="<your-token>"

terraform init
terraform plan
# terraform apply -auto-approve
```

This config contains a `data.databricks_current_user` data source which validates the provider is authenticated.

Notes

- The provider version in `versions.tf` can be updated as new releases are available.
- For Azure/Microsoft Managed Databricks or other auth flows, see the Databricks provider docs: https://registry.terraform.io/providers/databricks/databricks/latest/docs

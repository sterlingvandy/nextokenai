# Example: read the current Databricks user to validate provider
data "databricks_current_user" "me" {}

output "databricks_user" {
  value       = data.databricks_current_user.me
  description = "Information about the current authenticated Databricks user (for diagnostics)."
}

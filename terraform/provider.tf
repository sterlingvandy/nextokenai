provider "databricks" {
  # The provider can be configured via env variables or provider block.
  # We read variables so users can pass them via CLI or env file if they prefer.
  host  = var.databricks_host != "" ? var.databricks_host : null
  token = var.databricks_token != "" ? var.databricks_token : null
}

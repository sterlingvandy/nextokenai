# Optional defaults and hints
variable "databricks_host" {
  type        = string
  description = "Databricks workspace host (optional). If not provided, uses env var DATABRICKS_HOST."
  default     = ""
}

variable "databricks_token" {
  type        = string
  description = "Databricks PAT (optional). If not provided, uses env var DATABRICKS_TOKEN."
  default     = ""
}

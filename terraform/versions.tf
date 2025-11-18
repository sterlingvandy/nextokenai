terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.9" # pick a stable major version; update as needed
    }
  }

  required_version = ">= 1.0"
}

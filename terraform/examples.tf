# Databricks example resources (commented by default)
#
# These are safe example resource blocks you can uncomment to try creating
# real resources in Databricks. Because they are commented, `terraform validate`
# will still succeed without credentials and won't create anything on apply.
#
# To enable an example, remove the leading '#' from the lines you want to create
# and run `terraform plan` / `terraform apply` once you have the correct auth.

# ---------------------------
# Example: simple cluster
# ---------------------------
# resource "databricks_cluster" "example" {
#   cluster_name            = "example-cluster"
#   spark_version           = "13.1.x-scala2.12"
#   node_type_id            = "Standard_DS3_v2" # change according to cloud provider
#   autotermination_minutes = 15
#   num_workers             = 2
# }

# ---------------------------
# Example: job that runs a notebook
# ---------------------------
# resource "databricks_job" "example" {
#   name = "example-job"
#   new_cluster {
#     spark_version = "13.1.x-scala2.12"
#     node_type_id  = "Standard_DS3_v2"
#     num_workers   = 2
#   }
#   notebook_task {
#     notebook_path = "/Users/example@example.com/ExampleNotebook"
#   }
# }

# ---------------------------
# Example: workspace group (identity example)
# ---------------------------
# resource "databricks_group" "example" {
#   display_name = "example-group"
# }

# ---------------------------
# Example: make job depend on cluster (explicit use)
# ---------------------------
# resource "databricks_job" "job_with_existing_cluster" {
#   name = "job-with-existing-cluster"
#   existing_cluster_id = databricks_cluster.example.cluster_id
#   notebook_task {
#     notebook_path = "/Users/example@example.com/AnotherNotebook"
#   }
#   depends_on = [databricks_cluster.example]
# }

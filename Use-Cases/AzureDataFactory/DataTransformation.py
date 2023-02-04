# Load data from Azure Blob Storage into Databricks
df = spark.read.parquet("wasbs://<container_name>@<account_name>.blob.core.windows.net/<file_path>")

# Perform data transformation
df = df.filter(df["column_name"] > 0)

# Write transformed data back to Azure Blob Storage
df.write.mode("overwrite").parquet("wasbs://<container_name>@<account_name>.blob.core.windows.net/<file_path>")

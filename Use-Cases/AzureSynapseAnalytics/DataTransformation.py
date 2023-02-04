# Load data from Azure Synapse Analytics into Databricks
df = spark.read.table("synapse_database.table_name")

# Perform data transformation
df = df.filter(df["column_name"] > 0)

# Write transformed data back to Azure Synapse Analytics
df.write.mode("overwrite").table("synapse_database.table_name")

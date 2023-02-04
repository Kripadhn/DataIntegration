from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("BatchDataProcessing").getOrCreate()

# Read data from a source file
data = spark.read.format("csv").option("header", "true").load("source.csv")

# Perform some transformations on the data
transformedData = data.filter(data["columnA"] > 100)

# Write the transformed data to a target file
transformedData.write.format("csv").option("header", "true").mode("overwrite").save("target.csv")

# Stop the Spark session
spark.stop()

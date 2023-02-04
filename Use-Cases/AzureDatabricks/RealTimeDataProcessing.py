from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a Spark session
spark = SparkSession.builder.appName("RealTimeDataProcessing").getOrCreate()

# Read data from a real-time source
data = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "topic").load()

# Perform some transformations on the data
transformedData = data.selectExpr("cast (value as string) as json").select(getField("json").alias("json")) \
  .select(from_json("json", schema).alias("data")).select("data.*") \
  .filter("columnA > 100")

# Write the transformed data to a target file
query = transformedData.writeStream.outputMode("append").format("parquet").option("path", "target/").option("checkpointLocation", "checkpoint/").start()

# Wait for the query to finish
query.awaitTermination()

# Stop the Spark session
spark.stop()

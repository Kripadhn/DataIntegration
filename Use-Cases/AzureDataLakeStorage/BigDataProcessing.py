from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a Spark session
spark = SparkSession.builder.appName("BigDataProcessing").getOrCreate()

# Read data from a large file in ADLS
data = spark.read.format("csv").option("header", "true").load("adl://<adls-account-name>.azuredatalakestore.net/input/data.csv")

# Perform some transformations on the data
transformedData = data.filter("columnA > 100").groupBy("columnB").agg(avg("columnC"), max("columnD"))

# Write the transformed data to a file in ADLS
transformedData.write.format("csv").option("header", "true").mode("overwrite").save("adl://<adls-account-name>.azuredatalakestore.net/output/")

# Stop the Spark session
spark.stop()

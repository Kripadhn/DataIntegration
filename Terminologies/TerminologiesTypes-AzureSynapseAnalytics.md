Azure Synapse Analytics:
# - Workspace: A single Azure Synapse workspace is the unit of management for all data and metadata across your big data and data warehousing scenarios.

Example:
# Creating a new Synapse workspace
from azureml.core import Workspace

ws = Workspace.create(
name='myworkspace',
subscription_id='<subscription-id>',
resource_group='<resource-group>',
create_resource_group=True,
location='<location>'
)


# - Spark Tables: A Spark table is a data structure that allows you to store and manipulate large amounts of data in a Spark cluster.

Example:

# Loading data into Spark table
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["name", "age"])
df.createOrReplaceTempView("people")

# Querying Spark table
result = spark.sql("SELECT * FROM people")
result.show()


# - Data Flows: Data flows provide a visual, no-code experience for transforming and cleansing your data using Spark in Azure Synapse Analytics.

Example:

# Creating a data flow
from azureml.datawarehousing.models import DataFlow

df = DataFlow.create(
name='mydataflow',
workspace=ws
)


# - Datasets: Datasets provide a way to store structured data in the Azure Synapse Analytics workspace, so it can be easily shared and reused across multiple Spark jobs, notebooks, and data flows.

Example:
# Creating a dataset
from azureml.datawarehousing.datasets import Dataset

ds = Dataset.create_from_dataframe(
dataframe=df,
name='mydataset',
workspace=ws
)


# - Notebooks: Notebooks provide a way to interact with your data and code in a web-based interface, which supports multiple programming languages such as Python, R, and SQL.

Example:
from azureml.datawarehousing.notebook import Notebook

nb = Notebook.create(
name='mynotebook',
workspace=ws
)

nb.run("spark.sql("SELECT * FROM mydataset")")


These are just a few examples of the common terminologies used in Azure data integration. The implementation and code may vary depending on the use case and specific requirements.


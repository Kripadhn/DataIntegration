Inputs: Inputs are the sources of data that Stream Analytics reads from. Inputs can be either an event hub, IoT hub, or a Blob storage.
Example:
# Defining an input source in Stream Analytics job
SELECT *
INTO [output]
FROM [input]

Queries: Queries are used to process data from the inputs and to define the transformations to be applied on the data.
Example:
# Defining a query in Stream Analytics job
SELECT AVG(value) as average, System.Timestamp as time
INTO [output]
FROM [input]
GROUP BY TumblingWindow(second, 10)

Outputs: Outputs are the destinations where Stream Analytics writes the processed data. Outputs can be an Azure Event Hub, an Azure IoT Hub, an Azure Service Bus, or an Azure Blob storage.
Example:
# Defining an output destination in Stream Analytics job
SELECT *
INTO [output]
FROM [input]

Functions: Functions are used to perform a specific operation or calculation on the data, such as aggregate functions, string functions, and math functions.
Example:
# Using functions in a Stream Analytics query
SELECT AVG(value) as average, System.Timestamp as time
INTO [output]
FROM [input]
WHERE value > 50
GROUP BY TumblingWindow(second, 10)

Stream Analytics Job: A Stream Analytics job is a group of inputs, outputs, and queries that define the data processing logic for your data.
Example:
# Creating a Stream Analytics job
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient
from azure.mgmt.resource import ResourceManagementClient

sa_client = StreamAnalyticsManagementClient(credentials, subscription_id)
resource_client = ResourceManagementClient(credentials, subscription_id)

job_name = "mystreamanalyticsjob"
resource_group_name = "myresourcegroup"
job_create_param = sa_client.streaming_jobs.create_or_update(
  resource_group_name,
  job_name,
  {
    "location": "westus",
    "sku": {
      "name": "standard"
    },
    "tags": {
      "tag1": "value1",
      "tag2": "value2"
    },
    "inputs": [
      {
        "name": "input",
        "type": "Stream",
        "datasource": {
          "type": "Microsoft.ServiceBus/EventHub",
          "eventhub": {
            "name": "myeventhub",
            "connection_string": "Endpoint=sb://mynamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<shared-access-key>"
          }
        }
      }
    ],
    "outputs": [
      {
        "name": "output",
       
"type": "Blob",
"datasource": {
"type": "Microsoft.Storage/Blob",
"store_location": "westus2",
"account_name": "myaccount",
"container": "mycontainer",
"access_key": "<access-key>"
}
}
],
"transformation": {
"name": "StreamingJob",
"streaming_units": 1,
"query": "SELECT * INTO [output] FROM [input]"
}
}
)
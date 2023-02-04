Azure Data Factory:

Linked Services: Connections to data sources and destinations that are defined in JSON format.
Example:
{
  "name": "AzureStorageLinkedService",
  "type": "AzureStorage",
  "typeProperties": {
    "connectionString": "DefaultEndpointsProtocol=https;AccountName=<account-name>;AccountKey=<account-key>"
  }
}


Data Flows: Visual, no-code data transformations that can be used to cleanse, shape, and transform data.
Example:
{
  "name": "RemoveSpecialCharacters",
  "type": "Expression",
  "dependsOn": [    "[datasource]"  ],
  "typeProperties": {
    "expression": "replace(replace(replace(replace(replace(replace(<column-name>, ' ', ''), '#', ''), '@', ''), '!', ''), '$', ''), '%', '')"
  }
}

Datasets: Define the structure and content of data that is used as inputs and outputs for data factory pipelines.
Example:
{
  "name": "InputDataset",
  "type": "AzureSqlTable",
  "linkedServiceName": "AzureSqlLinkedService",
  "typeProperties": {
    "tableName": "<table-name>"
  },
  "schema": [
    {
      "name": "<column-name-1>",
      "type": "<column-type-1>"
    },
    {
      "name": "<column-name-2>",
      "type": "<column-type-2>"
    }
  ]
}


Pipelines: Define data movement and transformation activities that are executed by the data factory.
Example:
{
  "name": "Pipeline1",
  "type": "Microsoft.DataFactory/factories/pipelines",
  "dependsOn": [
    "[linkedService1]",
    "[dataset1]",
    "[dataset2]"
  ],
  "properties": {
    "description": "Example pipeline",
    "activities": [
      {
        "type": "Copy",
        "typeProperties": {
          "source": {
            "type": "AzureSqlTableSource",
            "sqlReaderQuery": "SELECT * FROM <table-name>"
          },
          "sink": {
            "type": "AzureBlobSink",
            "writeBatchSize": 0,
            "writeBatchTimeout": "00:00:00"
          }
        },
        "inputs": [
          {
            "referenceName": "<input-dataset-name>",
            "type": "DatasetReference"
          }
        ],
        "outputs": [
          {
            "referenceName": "<output-dataset-name>",
                  "type": "DatasetReference"
         }
       ],
       "policy": {
         "timeout": "01:00:00",
         "concurrency": 1,
         "executionPriorityOrder": "NewestFirst",
         "retry": 3
       },
       "name": "CopyData"
     }
   ]
 }




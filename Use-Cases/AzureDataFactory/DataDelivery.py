from azure.common import AzureHttpError
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *

# Connect to Azure Data Factory
df_client = DataFactoryManagementClient(credentials, subscription_id)

# Create a pipeline with a single activity (copy data)
pipeline = PipelineResource(
activities=[
CopyActivity(
name='Copy Data',
source=BlobSource(
type='BlobSource',
blob_prefix=None
),
sink=SqlSink(
type='SqlSink',
sql_writer_stored_procedure_name=None,
sql_writer_stored_procedure_parameters=None,
sql_writer_table_type=None,
sql_writer_table_name=None,
sql_writer_database=None
)
)
],
annotations=[]
)
# Create the pipeline in Azure Data Factory
df_client.pipelines.create_or_update(resource_group_name, data_factory_name, 'pipeline_name', pipeline)
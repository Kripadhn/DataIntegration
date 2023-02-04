-- Create a database in Azure Synapse Analytics to share data
CREATE DATABASE SharedData;

-- Create a table in the SharedData database to store data
CREATE TABLE SharedData.SalesData
(
    Date datetime,
    Region varchar(100),
    SalesAmount float
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = ROUND_ROBIN
);

-- Copy data from the source database to the SharedData database
INSERT INTO SharedData.SalesData
SELECT Date, Region, SalesAmount
FROM SourceDatabase.Sales;

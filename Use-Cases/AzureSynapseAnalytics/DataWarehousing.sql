-- Create a data warehouse in Azure Synapse Analytics
CREATE DATABASE DataWarehouse;

-- Create a table to store data in the data warehouse
CREATE TABLE DataWarehouse.Sales
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

-- Load data into the Sales table
INSERT INTO DataWarehouse.Sales
SELECT Date, Region, SalesAmount
FROM SourceDatabase.

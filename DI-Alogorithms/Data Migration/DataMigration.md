Here is an example of a data migration algorithm in Python that migrates data from a CSV file to a database table:

In this example, the data is first read from a CSV file and the headers are used to create a table in a PostgreSQL database. Then, the data is inserted into the table row by row. Note that the psycopg2 library is used to connect to the PostgreSQL database.
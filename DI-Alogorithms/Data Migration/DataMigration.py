import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="mydatabaseuser",
    password="mypassword"
)
cursor = conn.cursor()

# Open the CSV file
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    
    # Create the table in the database
    create_table_query = f"CREATE TABLE data ({','.join(headers)})"
    cursor.execute(create_table_query)
    
    # Insert the data from the CSV file into the database table
    insert_query = f"INSERT INTO data VALUES ({','.join(['%s'] * len(headers))})"
    for row in reader:
        cursor.execute(insert_query, row)

# Commit the changes and close the connection
conn.commit()
conn.close()

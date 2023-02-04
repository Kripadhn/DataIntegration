Data Extraction: The process of retrieving data from one or multiple sources is called data extraction. The problem is that data may reside in different sources, in different formats, and may be difficult to access or may be inconsistent.
Solution: To solve these issues, data extraction is performed, which involves data transfer from one or multiple sources to a central data storage location. Code example in Python to extract data from a CSV file and store it in a database:

Python:-

import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("INSERT INTO table_name (column1, column2, column3) VALUES (%s, %s, %s)", row)

conn.commit()
cursor.close()
conn.close()

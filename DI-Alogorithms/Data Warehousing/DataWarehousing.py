import sqlite3

# Connect to the database
conn = sqlite3.connect('warehouse.db')
c = conn.cursor()

# Create the fact table
c.execute("CREATE TABLE sales_fact (id INTEGER PRIMARY KEY, date DATE, product_id INTEGER, store_id INTEGER, sales INTEGER)")

# Create the dimension tables
c.execute("CREATE TABLE product_dim (id INTEGER PRIMARY KEY, product_name TEXT, category TEXT)")
c.execute("CREATE TABLE store_dim (id INTEGER PRIMARY KEY, store_name TEXT, location TEXT)")

# Insert data into the dimension tables
c.execute("INSERT INTO product_dim (id, product_name, category) VALUES (1, 'Product 1', 'Category 1')")
c.execute("INSERT INTO product_dim (id, product_name, category) VALUES (2, 'Product 2', 'Category 2')")
c.execute("INSERT INTO store_dim (id, store_name, location) VALUES (1, 'Store 1', 'Location 1')")
c.execute("INSERT INTO store_dim (id, store_name, location) VALUES (2, 'Store 2', 'Location 2')")

# Insert data into the fact table
c.execute("INSERT INTO sales_fact (id, date, product_id, store_id, sales) VALUES (1, '2021-01-01', 1, 1, 100)")
c.execute("INSERT INTO sales_fact (id, date, product_id, store_id, sales) VALUES (2, '2021-01-02', 2, 2, 200)")

# Commit changes and close the connection
conn.commit()
conn.close()

# In this example, we create a SQLite database to store the data. 
# The fact table sales_fact stores the sales data, and the dimension tables product_dim and store_dim store information 
# about products and stores, respectively. 
# The Star Schema is created by joining the fact table with the dimension tables on the key columns.
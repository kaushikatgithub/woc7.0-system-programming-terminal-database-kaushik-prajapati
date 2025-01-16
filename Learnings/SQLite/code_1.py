import sqlite3 as sq

# conn = sq.connect(":memory:")

# connection_to_database, this database is temporary i.e. available only through the lifecycle of the code
conn = sq.connect("customers.db")

# To prform any changes to the database, we need a cursor. Every changes are done via cursor
cur = conn.cursor()

# Create a table
cur.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text  
        )""")
print("Table created successfully")
# Datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Commit our command
conn.commit()

# Close our connection after use
conn.close()
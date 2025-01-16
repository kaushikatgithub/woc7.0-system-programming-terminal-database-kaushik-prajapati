import sqlite3 as sq
import pandas as pd

conn = sq.connect("customers.db")

cur = conn.cursor()

# data = cur.execute("SELECT rowid, * FROM customers  WHERE email='kaushik@gmail.com'")
# df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
# print(df)

data = cur.execute("SELECT rowid, * FROM customers WHERE email LIKE '%@yahoo%'")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)

conn.commit()
conn.close()
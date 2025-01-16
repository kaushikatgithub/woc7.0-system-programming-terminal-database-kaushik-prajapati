import sqlite3 as sq
import pandas as pd

conn = sq.connect("customers.db")

cur = conn.cursor()

data = cur.execute("SELECT rowid, * FROM customers")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)
# print(cur.fetchone())
# print(cur.fetchmany(3))
# print(cur.fetchall())

conn.commit()
conn.close()
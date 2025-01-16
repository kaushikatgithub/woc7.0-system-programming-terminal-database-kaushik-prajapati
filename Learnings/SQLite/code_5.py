import sqlite3 as sq
import pandas as pd

conn = sq.connect("customers.db")

cur1 = conn.cursor()
data = cur1.execute("SELECT rowid, * FROM customers")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)

cur2 = conn.cursor()
cur2.execute("""UPDATE customers SET first_name = 'Kaushik' WHERE first_name = 'Rahul'""")
print("\n")

data = cur2.execute("SELECT rowid, * FROM customers")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)

conn.commit()
conn.close()
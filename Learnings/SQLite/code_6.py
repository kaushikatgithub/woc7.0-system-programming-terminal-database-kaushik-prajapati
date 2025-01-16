import sqlite3 as sq
import pandas as pd

conn = sq.connect("customers.db")

cur1 = conn.cursor()
data = cur1.execute("SELECT rowid, * FROM customers")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)

cur2 = conn.cursor()
cur2.execute("""DELETE FROM customers WHERE first_name = 'Kaushik'""")
print("\n")

data = cur2.execute("SELECT rowid, * FROM customers")
df = pd.DataFrame(data, columns = ["pkey", "first_name", "last_name", "email"])
print(df)

# We can use ASC, and DESC with ORDER BY 
# AND and OR are use for multiple conditioning
# We can limit the number of results using LIMIT keyword

conn.commit()
conn.close()
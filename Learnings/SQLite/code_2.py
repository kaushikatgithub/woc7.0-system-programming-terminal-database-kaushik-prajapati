import sqlite3 as sq

conn = sq.connect("customers.db")

cur = conn.cursor()

customers = [
    ('Hemal', 'Dholakiya', 'hemal@yahoo.com'),
    ('Meet', 'Thakker', 'meet@yahoo.com'),
    ('Mahideepsinh', 'Zala', 'mahideepsinh@yahoo.com'),
]

# cur.execute("""INSERT INTO customers VALUES 
#             ('Kaushik', 'Prajapati', 'kaushik@gmail.com'), 
#             ('Gautam', 'Prajapati', 'gautam@gmail.com')
#             """)

# ? is a placeholder for data   
cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)

print("Data inserted successfully!")
conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect("db/mydatabase2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

users = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 22)
]

cursor.executemany(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    users
)

cursor.execute(
    "SELECT * FROM users WHERE age > ?",
    (24,)
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
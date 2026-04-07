import sqlite3

conn = sqlite3.connect("db/mydatabase1.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO users (name, age)
VALUES ('Alice', 25)
""")

cursor.execute("""
INSERT INTO users (name, age)
VALUES ('Bob', 30)
""")

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
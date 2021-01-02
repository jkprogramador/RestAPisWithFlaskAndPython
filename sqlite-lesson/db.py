import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

create_table = "CREATE TABLE users ( \
id INTEGER PRIMARY KEY NOT NULL, \
username VARCHAR(255) NOT NULL UNIQUE, \
password VARCHAR(255) NOT NULL \
)"

cursor.execute(create_table)

users = [
    ("jose", "123",),
    ("rob", "123",)
]
insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

conn.commit()
conn.close()

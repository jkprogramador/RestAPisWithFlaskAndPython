import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE users")

create_table = "CREATE TABLE users ( \
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
username VARCHAR(255) NOT NULL UNIQUE, \
password VARCHAR(255) NOT NULL \
)"

cursor.execute(create_table)

users = [
    (1, "jose", "123",),
    (2, "rob", "123",)
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

conn.commit()
conn.close()

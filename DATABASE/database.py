import sqlite3



username = "jim"
password = "123"
database_name = "database.db"
table_name = "user_table"


connection = sqlite3.connect(database_name)
cursor = connection.cursor()


query = f"INSERT INTO {table_name} (username, password) VALUES ({username}, {password});"

cursor.execute(query, (username, password))


connection.commit()


print(f"User '{username}' added successfully.")


connection.close()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

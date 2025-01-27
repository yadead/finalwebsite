import sqlite3
database_name = "

username = "jim"
password = "123"
database_name = "database.db"
table_name = "user_table"


connection = sqlite3.connect(database_name)
cursor = connection.cursor()


query = f"INSERT INTO user_table (username, password) 
        VALUES ({username}, {password};"

cursor.execute(query, (username, password))


connection.commit()


print(f"User '{username}' added successfully.")


connection.close()
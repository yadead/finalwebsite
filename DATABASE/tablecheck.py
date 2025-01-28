import sqlite3

# Connect to the new database
connection = sqlite3.connect("DATABASE\database.db")
cursor = connection.cursor()

# Insert data
cursor.execute("INSERT INTO user_table (username, password) VALUES (?, ?)", ("jim", "123"))
connection.commit()

# Check table content
cursor.execute("SELECT * FROM user_table;")
rows = cursor.fetchall()
print("Table content:", rows)

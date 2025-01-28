import sqlite3
import os

database_name = "DATABASE/database.db"
table_name = "user_table"
print("Database path:", os.path.abspath(database_name))

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        username TEXT,
        password TEXT
    );
""")
connection.commit()

def signup(username, password):
    query = f"INSERT INTO {table_name} (username, password) VALUES (?, ?);"
    cursor.execute(query, (username, password))
    connection.commit()

def signin(username, password):
    """Check if a user exists in the database."""
    query = f"SELECT * FROM {table_name} WHERE username = ? AND password = ?;"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result is not None

import sqlite3
import os

database_name = "DATABASE/database.db"
table_name = "diary_entry"
print("Database path:", os.path.abspath(database_name))

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        Developer TEXT,
        Project TEXT,
        Start_Time TEXT,
        End_Time TEXT,
        Diary_Entry TEXT,
        Time_Worked TEXT,
        Repo TEXT,
        Developer_Notes TEXT

    );
""")
connection.commit()

def diary_entry(Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes ):
    query = f"INSERT INTO {table_name} (Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
    cursor.execute(query, (Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes))
    connection.commit()


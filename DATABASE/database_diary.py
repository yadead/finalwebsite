import sqlite3
import os

database_name = "DATABASE/database.db"
table_name = "diary_entry"
print("Database path:", os.path.abspath(database_name))

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        Entry_ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

def diary_entry(Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes):
    query = f"""
        INSERT INTO {table_name} (Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(query, (Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes))
    connection.commit()
    last_id = cursor.lastrowid
    return last_id

def insert_id_only(entry_id):
    query = f"INSERT INTO {table_name} (Entry_ID) VALUES (?);"
    cursor.execute(query, (entry_id,))
    connection.commit()
    return

def sdevname(sdev_name_choice): 
    query = f"SELECT Entry_ID, Developer, Project, Diary_Entry FROM {table_name} WHERE Developer = ?"
    cursor.execute(query, (sdev_name_choice,))
    dev_name_results = cursor.fetchall()
    return dev_name_results 

def sCHOICEID(choiceid):
    query = f"SELECT Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes FROM {table_name} WHERE Entry_ID = ?;"
    cursor.execute(query, (choiceid,))
    return cursor.fetchone()

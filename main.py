from DATABASE.database import signup, signin
from DATABASE.database_diary import diary_entry
from datetime import datetime
import math


def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    signup(username, password)
    print(f"User '{username}' has been signed up")

def sign_in():
    username = input("Username: ")
    password = input("Password: ")
    if signin(username, password):
        print(f"{username} has been logged in")
        menu2()
    else:
        print("Invalid username or password. Please try again.")

def Create_entry():
        Developer = input("Developer Name: ")
        Project = input("Project Name: ")
        time_format = "%H:%M %d/%m/%Y"
        Start_Time = input("Start Time (hh:mm dd/mm/yyyy): ")
        End_Time = input("End Time (hh:mm dd/mm/yyyy): ")
        start_dt = datetime.strptime(Start_Time, time_format)
        end_dt = datetime.strptime(End_Time, time_format)
        Time_Worked = end_dt - start_dt
        total_minutes = Time_Worked.total_seconds() / 60
        rounded_minutes = math.ceil(total_minutes / 15) * 15
        rounded_hours = rounded_minutes / 60
        now = datetime.now()
        Diary_Entry = now.strftime("%H:%M %d/%B/%Y")
        print(f"Diary_Entry: {Diary_Entry}")
        Time_Worked = rounded_hours
        print(f"Time Worked: {Time_Worked} hours")
        Repo = input("Repository Link: ")
        Developer_Notes = input("Developer Notes: ")
        diary_entry(Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes)


def menu():
    while True:
        choice = input("Choose an option:\n1. Sign In\n2. Sign Up\n3. Exit\n")
        if choice == "1":
            sign_in()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def menu2():
    while True:
        choice = input("Choose an option:\n1. Create Entry\n2. Lookup Entry\n3. Sign Out\n")
        if choice == "1":
            Create_entry()
        elif choice == "2":
            Lookup_entry()
        elif choice == "3":
            menu()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

menu()
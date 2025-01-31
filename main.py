from DATABASE.database import signup, signin
from DATABASE.database_diary import diary_entry, sdevname
from datetime import datetime
import math


def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    signup(username, password)
    print(f"User '{username}' has been signed up")

def sign_in():
    global devname
    devname = input("Username: ")
    username = devname
    password = input("Password: ")
    if signin(username, password):
        print(f"{username} has been logged in")
        menu2()
    else:
        print("Invalid username or password. Please try again.")

def Create_entry():
    print(last_id)
    Developer = devname
    print(f"Developer: {Developer}")
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
    Time_Worked = rounded_hours
    print(f"Time Worked: {Time_Worked} hours")
    now = datetime.now()
    Diary_Entry = now.strftime("%H:%M %d/%B/%Y")
    print(f"Diary_Entry: {Diary_Entry}")
    Repo = input("Repository Link: ")
    Developer_Notes = input("Developer Notes: ")
    diary_entry(Developer, Project, Start_Time, End_Time, Diary_Entry, Time_Worked, Repo, Developer_Notes)
    print("Diary entry added")

def sdeveloper_name():
    global sdev_name_choice
    sdev_name_choice = input("Developer name: ")  

    dev_name_results = sdevname(sdev_name_choice)

    if dev_name_results:  
        for dev in dev_name_results:  
            print(" || ".join(map(str, dev)))
    else:
        print("No results found. Please try again.")

    respon




# def sproject_name():




# def sdiary_entry_time():


def search_entry():
    while True: 
        choice = input("search by:\n1. Developer Name\n2. Project Name\n3. Diary entry time\n4. Go Back\n")
        if choice == "1":
            sdeveloper_name()
        elif choice == "2":
            sproject_name()
        elif choice == "3":
            sdiary_entry_time()
        elif choice == "4":
            menu2()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def delete_entry():
    print("nothingdoneyet")


def menu():
    while True:
        choice = input("Choose an option:\n1. Sign In\n2. Sign Up\n3. Exit\n")
        if choice == "1":
            sign_in()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def menu2():
    while True:
        choice = input("Choose an option:\n1. Create Entry\n2. Lookup Entry\n3. Delete Entry\n4. Sign Out\n")
        if choice == "1":
            Create_entry()
        elif choice == "2":
            search_entry()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            menu()
            sign_in(devname) == None
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

menu()
from DATABASE.database import signup, signin

def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    signup(username, password)
    print(f"User '{username}' has been signed up")

def sign_in():
    username = input("Username: ")
    password = input("Password: ")
    if signin(username, password):
        print(f"{username}has been logged in")
    else:
        print("Invalid username or password. Please try again.")

def menu():
    while True:
        choice = input("Choose an option:\n1. Sign In\n2. Sign Up\n3. Exit\n")
        if choice == "1":
            sign_in()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

menu()
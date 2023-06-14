from register import register
from login import login
from snake import snake
from top_scores import top_scores

def main_menu():
    print("Welcome to Your Terminal Program!")
    print("Please choose an option:")
    print("1. Login")
    print("2. Register")
    print("3. Show top scores")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login_result = login()
        if login_result is not None and login_result[0]:
            snake(login_result[1])
    elif choice == "2":
        register()
    elif choice == "3":
        top_scores()
    elif choice == "4":
        print("Thank you for using Your Terminal Program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_game():
    print("Game is starting...")


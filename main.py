from meal_planner.app import (
    setup_terminal_ui,
    onboard_user,
    update_user_preferences,
    delete_user_preferences,
)

if __name__ == "__main__":
    setup_terminal_ui()

    while True:
        print(
            "\nOptions:\n1. Onboard\n2. Update Preferences\n3. Delete Preferences\n4. Quit"
        )
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1" or choice == "onboard":
            onboard_user()
        elif choice == "2" or choice == "update preferences":
            update_user_preferences()
        elif choice == "3" or choice == "delete preferences":
            delete_user_preferences()
        elif choice == "4" or choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# FoodieAIdvisor - An AI-powered terminal-based recipe advisor
from meal_planner.helpers import (
    setup_terminal_ui,
    select_user,
)
from meal_planner.user_preferences import (
    update_user_preferences,
    delete_user_preferences,
)
from meal_planner.onboarding import onboard_user
from meal_planner.inventory_management import (
    add_ingredients,
    list_ingredients,
    delete_ingredient,
    set_expiration_date,
)
from meal_planner.recommendations import get_recommendations


def app():
    setup_terminal_ui()

    try:
        active_user = select_user()
        print(f"Welcome, {active_user}!")

        while True:
            print("\nOptions:")
            print("0. Recommendations")
            print("1. Onboard")
            print("2. Update Preferences")
            print("3. Delete Preferences")
            print("4. Add Ingredients")
            print("5. List Ingredients")
            print("6. Delete Ingredient")
            print("7. Set Expiration Date for Ingredient")
            print("8. Quit")
            print("Enter 'help' to see more details.\n")

            choice = input("Enter your choice: ").strip().lower()

            if choice == "help":
                print("Help is on the way!")
            elif choice == "0":
                print(
                    "Get recommendations based off of your current inventory and tastes."
                )
                cuisine = input(
                    "Enter the cuisine that you would like to eat right now: "
                ).strip()
                get_recommendations(cuisine)

            elif choice in ["1", "onboard"]:
                onboard_user()
            elif choice in ["2", "update preferences"]:
                update_user_preferences()
            elif choice in ["3", "delete preferences"]:
                delete_user_preferences()
            elif choice in ["4", "add ingredients"]:
                add_ingredients()
            elif choice in ["5", "list ingredients"]:
                list_ingredients()
            elif choice in ["6", "delete ingredient"]:
                delete_ingredient()
            elif choice in ["7", "set expiration"]:
                set_expiration_date()
            elif choice in ["8", "q", "quit"]:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\nExiting FoodieAIdvisor... Goodbye!")

import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def update_user_preferences():
    """Update user food preferences and restrictions."""

    username = input("Enter your username: ").strip()

    # Check if the username exists in the database
    # TODO: move this to a function in another file
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT preferences, dietary_restrictions FROM users WHERE username=?",
            (username,),
        )
        user = cursor.fetchone()

        if user:
            old_preferences, old_dietary_restrictions = user

            # Ask the user to update their details
            additional_preferences = input(
                "Add more favorite cuisines or dishes (leave blank to skip): "
            ).strip()
            additional_dietary_restrictions = input(
                "Add more dietary restrictions (leave blank to skip): "
            ).strip()

            # Combine the new details with the existing ones
            new_preferences = old_preferences + (
                ", " + additional_preferences if additional_preferences else ""
            )
            new_dietary_restrictions = old_dietary_restrictions + (
                ", " + additional_dietary_restrictions
                if additional_dietary_restrictions
                else ""
            )

            # Update the user details in the database
            cursor.execute(
                """
                UPDATE users
                SET preferences=?, dietary_restrictions=?
                WHERE username=?
            """,
                (new_preferences, new_dietary_restrictions, username),
            )

            print("User preferences updated successfully!")
        else:
            print("Username not found. Please check and try again.")


def delete_user_preferences():
    """Delete specific user food preferences and restrictions."""

    username = input("Enter your username: ").strip()

    # Check if the username exists in the database
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT preferences, dietary_restrictions FROM users WHERE username=?",
            (username,),
        )
        user = cursor.fetchone()

        if user:
            preferences, dietary_restrictions = user

            # Display current preferences and restrictions
            print(f"Current Preferences: {preferences}")
            print(f"Current Dietary Restrictions: {dietary_restrictions}")

            # Ask the user which ones to remove
            preferences_to_delete = (
                input("Enter preferences to delete (comma-separated): ")
                .strip()
                .split(",")
            )
            restrictions_to_delete = (
                input(
                    "Enter dietary restrictions to delete (comma-separated): "
                )
                .strip()
                .split(",")
            )

            # Remove the specified preferences and restrictions
            new_preferences = ", ".join(
                p.strip()
                for p in preferences.split(",")
                if p.strip() not in preferences_to_delete
            )
            new_dietary_restrictions = ", ".join(
                r.strip()
                for r in dietary_restrictions.split(",")
                if r.strip() not in restrictions_to_delete
            )

            # Update the user details in the database
            cursor.execute(
                """
                UPDATE users
                SET preferences=?, dietary_restrictions=?
                WHERE username=?
            """,
                (new_preferences, new_dietary_restrictions, username),
            )

            print("User preferences updated successfully!")
        else:
            print("Username not found. Please check and try again.")

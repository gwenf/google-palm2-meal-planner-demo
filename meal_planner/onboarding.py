import sqlite3
from meal_planner.helpers import (
    get_active_user_id,
)

DATABASE_PATH = "foodieaidvisor.db"


def onboard_user():
    """Gather initial user preferences, dietary restrictions, and ingredients for the active user."""

    user_id = get_active_user_id()
    if not user_id:
        print("No active user found. Please select or create a user first.")
        return

    # Ask the user for their preferences and dietary restrictions
    preferences = input(
        "What are your favorite cuisines or dishes? (e.g. Italian, Sushi): "
    ).strip()
    dietary_restrictions = input(
        "Do you have any dietary restrictions? (e.g. Vegetarian, Gluten-free): "
    ).strip()

    # Update the user details in the database
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users 
            SET preferences = ?, dietary_restrictions = ?
            WHERE id = ?
            """,
            (preferences, dietary_restrictions, user_id),
        )

        # Prompt the user to add ingredients to their inventory
        while True:
            ingredient = input(
                "Enter an ingredient you'd like to add (or 'done' to finish): "
            ).strip()
            if ingredient.lower() == "done":
                break
            cursor.execute(
                """
                INSERT INTO ingredients (user_id, name)
                VALUES (?, ?)
            """,
                (user_id, ingredient),
            )

        conn.commit()

    print("User onboarded successfully!")

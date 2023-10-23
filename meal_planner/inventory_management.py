import sqlite3

from meal_planner.helpers import get_active_user_id

DATABASE_PATH = "foodieaidvisor.db"


def add_ingredients():
    """Allow the user to add ingredients to their inventory."""
    user_id = get_active_user_id()
    ingredient = input("Enter the ingredient you'd like to add: ").strip()

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ingredients (user_id, name)
            VALUES (?, ?)
        """,
            (user_id, ingredient),
        )
        print(f"{ingredient} added successfully!")


def delete_ingredient():
    """Allow the user to delete an ingredient from their inventory."""
    user_id = get_active_user_id()
    ingredient = input("Enter the ingredient you'd like to delete: ").strip()

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM ingredients WHERE user_id=? AND name=?",
            (user_id, ingredient),
        )
        print(f"{ingredient} removed from your inventory!")


def list_ingredients():
    """List all ingredients in the user's inventory."""
    user_id = get_active_user_id()

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM ingredients WHERE user_id=?",
            (user_id,),
        )
        ingredients = cursor.fetchall()

        if ingredients:
            print("Your ingredients are:")
            for ingredient in ingredients:
                print("-", ingredient[0])
        else:
            print("You have no ingredients in your inventory.")


def set_expiration_date():
    """Allow the user to set expiration dates for ingredients."""
    user_id = get_active_user_id()
    ingredient = input(
        "Enter the ingredient you'd like to set an expiration date for: "
    ).strip()
    expiration_date = input("Enter the expiration date (YYYY-MM-DD): ").strip()

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE ingredients
            SET expiration_date=?
            WHERE user_id=? AND name=?
        """,
            (expiration_date, user_id, ingredient),
        )
        print(f"Expiration date for {ingredient} set to {expiration_date}!")

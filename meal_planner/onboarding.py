import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def onboard_user():
    """Gather initial user preferences and dietary restrictions."""

    # Ask the user for their details
    username = input("Enter your username: ").strip()
    preferences = input(
        "What are your favorite cuisines or dishes? (e.g. Italian, Sushi): "
    ).strip()
    dietary_restrictions = input(
        "Do you have any dietary restrictions? (e.g. Vegetarian, Gluten-free): "
    ).strip()

    # Store the user details in the database
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO users (username, preferences, dietary_restrictions)
                VALUES (?, ?, ?)
            """,
                (username, preferences, dietary_restrictions),
            )
            print("User onboarded successfully!")
        except sqlite3.IntegrityError:
            print(
                "Username already exists. Please choose a different username."
            )

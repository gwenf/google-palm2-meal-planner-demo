import sqlite3

from meal_planner.google_ai_interface import initialize_chat

DATABASE_PATH = "foodieaidvisor.db"


def get_recommendations(cuisine_choice):
    """Fetch recipe recommendations based on user preferences and inventory."""
    print("Fetching recommendations...")
    print(cuisine_choice)

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()

        # Fetch the active user's username from the active_user table
        cursor.execute("SELECT username FROM active_user LIMIT 1")
        active_username = cursor.fetchone()
        if not active_username:
            print("Error: No active user found.")
            return []

        # Get the user_id for the active user
        cursor.execute(
            "SELECT id FROM users WHERE username=?", (active_username[0],)
        )
        user_id = cursor.fetchone()
        if not user_id:
            print(f"Error: User ID for {active_username[0]} not found.")
            return []

    chat, parameters = initialize_chat(
        "swift-analogy-399402", "us-central1", user_id[0]
    )
    responses = chat.send_message_streaming(
        message=f"The cuisine I'm craving right now is {cuisine_choice}",
        **parameters,
    )
    for response in responses:
        # print(response)
        # print(type(response))
        print(response.text)
        # print(response.__dict__)
    return responses


def select_recipe():
    """Let the user select a preferred recipe from recommendations."""
    recommendations = get_recommendations()
    for idx, recommendation in enumerate(recommendations, 1):
        print(f"{idx}. {recommendation}")

    choice = int(input("Select a recipe by its number: "))
    selected_recipe = recommendations[choice - 1]
    print(f"You selected: {selected_recipe}")

    # You might want to do something more with the selected recipe, e.g., show details, steps, etc.
    return selected_recipe


def rate_recipe():
    """Allow the user to rate a recipe after trying it."""
    recipe_name = input(
        "Enter the name of the recipe you'd like to rate: "
    ).strip()
    rating = int(input("Rate the recipe on a scale of 1-5: "))

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO recipe_ratings (recipe_name, rating)
            VALUES (?, ?)
        """,
            (recipe_name, rating),
        )
        print(f"Thanks for rating {recipe_name}!")

    # Assuming there's a table called `recipe_ratings` with columns `recipe_name` and `rating`.

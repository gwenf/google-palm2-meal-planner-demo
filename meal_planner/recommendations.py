# TODO:
# 1. ~~Get the AI to fetch a summary of recommendations and you can select one~~
# 2. Then send the selection back to the AI for a list of ingredients and what
# you need to buy
# 3. Save the receipe into the database
# 4. Allow the user to rate the recipe to give feedback to the AI

import sqlite3

from meal_planner.google_ai_interface import initialize_chat

DATABASE_PATH = "foodieaidvisor.db"


def save_recipe_to_db(recipe_name, ingredients, instructions):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO recipes (name, ingredients, instructions)
            VALUES (?, ?, ?)
        """,
            (recipe_name, ingredients, instructions),
        )


def get_recommendations(cuisine_choice):
    """Fetch recipe recommendations based on user preferences and inventory."""
    print("Fetching recommendations...")

    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()

        # Fetch the active user's username and preferences
        cursor.execute(
            "SELECT users.username, user_id, preferences, dietary_restrictions FROM active_user JOIN users ON active_user.user_id = users.id LIMIT 1"
        )
        user_data = cursor.fetchone()
        if not user_data:
            print("Error: No active user found.")
            return []

        (
            active_username,
            active_user_id,
            preferences,
            dietary_restrictions,
        ) = user_data
        context = f"My name is {active_username}. I like {preferences}. I have {dietary_restrictions} dietary restrictions. The cuisine I'm craving right now is {cuisine_choice}."

    chat, parameters = initialize_chat(
        "swift-analogy-399402", "us-central1", active_user_id
    )
    responses = chat.send_message_streaming(message=context, **parameters)
    print("Recommendations:")
    print(responses)

    recommendations = []
    for response in responses:
        print(response)
        recommendations.append(response)

    return recommendations


def select_recipe():
    """Let the user select a preferred recipe from recommendations."""
    recommendations = get_recommendations()
    for idx, recommendation in enumerate(recommendations, 1):
        print(f"{idx}. {recommendation}")

    choice = int(input("Select a recipe by its number: "))
    selected_recipe = recommendations[choice - 1]
    print(f"You selected: {selected_recipe}")

    # TODO: show the ingredients and instructions for the selected recipe

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

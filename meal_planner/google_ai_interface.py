import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair
import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def initialize_chat(project_id: str, location: str, user_id: int):
    # Fetching user details and ingredients from SQLite
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT username, preferences FROM users WHERE id=?", (user_id,)
        )
        user_details = cursor.fetchone()

        cursor.execute(
            "SELECT name FROM ingredients WHERE user_id=?", (user_id,)
        )
        ingredients = cursor.fetchall()

    ingredient_example = ", ".join(
        [ingredient[0] for ingredient in ingredients]
    )
    context = f"My name is {user_details[0]}. My food preferences are {user_details[1]}. I currently have the following ingredients: {ingredient_example}. Please learn what I like to eat so you can give me tailored recommendations for my meal planning."

    example_text = (
        "I would like to eat korean food based off of the ingredients I have."
    )

    vertexai.init(project=project_id, location=location)

    chat_model = ChatModel.from_pretrained("chat-bison")

    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 512,
        "top_p": 0.95,
        "top_k": 40,
    }

    chat = chat_model.start_chat(
        context=context,
        examples=[
            InputOutputTextPair(
                input_text=example_text,
                output_text="Based on those ingredients, here are 3 recipes for meals you can try along with step by step instructions and a list of additional ingredients you will need to purchase. Let me know which one you would like to try so I can learn your preferences.",
            ),
        ],
    )

    return (chat, parameters)

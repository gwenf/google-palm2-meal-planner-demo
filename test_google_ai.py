import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair


def streaming_prediction(
    project_id: str,
    location: str,
) -> str:
    """Streaming Chat Example with a Large Language Model"""

    vertexai.init(project=project_id, location=location)

    chat_model = ChatModel.from_pretrained("chat-bison")

    parameters = {
        "temperature": 0.8,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    chat = chat_model.start_chat(
        context="My name is Gwen. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text="How many moons does Mars have?",
                output_text="The planet Mars has two moons, Phobos and Deimos.",
            ),
        ],
    )

    responses = chat.send_message_streaming(
        message="How many planets are there in the solar system?", **parameters
    )
    for response in responses:
        print(response.text)
    responses = chat.send_message_streaming(
        message="What day is it?", **parameters
    )
    for response in responses:
        print(response.text)
    responses = chat.send_message_streaming(
        message="Who is R2D2?", **parameters
    )
    for response in responses:
        print(response.text)


if __name__ == "__main__":
    streaming_prediction("swift-analogy-399402", "us-central1")

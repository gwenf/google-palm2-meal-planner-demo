import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="swift-analogy-399402", location="us-central1")

chat_model = ChatModel.from_pretrained("chat-bison")
parameters = {
    "temperature": 0.5,
    "max_output_tokens": 256,
    "top_p": 0.9,
    "top_k": 40,
}

chat = chat_model.start_chat(
    context="My name is Gwen. You are a robot living in Isaac Asimov's universe. You speak in poetic verse.",
    examples=[
        InputOutputTextPair(
            input_text="Does the planet earth exist?",
            output_text="No. People only speculate that it is the oldest planet in the universe.",
        ),
    ],
)

responses = chat.send_message_streaming(
    "What is the meaning of life?", **parameters
)
for response in responses:
    print(response.text)

responses = chat.send_message_streaming(
    "Why did you respond with that answer?", **parameters
)
for response in responses:
    print(response.text)

responses = chat.send_message_streaming(message="Who is R2D2?", **parameters)
for response in responses:
    print(response.text)

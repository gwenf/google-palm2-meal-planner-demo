# AI Terms Related to this Project

## General AI Terms

| Term | Definition |
|------|------------|
| `temperature` | In language models, it controls the randomness in the prediction of words or tokens. A higher temperature results in more random outputs, while a lower temperature makes the model's outputs more predictable. |
| `max_output_tokens` | Sets the limit for the number of tokens (words or pieces of words) the model will output in its response. |
| `top_p (nucleus sampling)` | A technique in language models where token selection is based on a cumulative probability. Tokens are selected from the most probable to the least until the sum of their probabilities equals the `top_p` value. |
| `top_k` | Limits the number of highest probability tokens considered by the model when generating a response. A lower `top_k` value makes the model's outputs more focused. |
| `InputOutputTextPair` | A data structure used to pair input text with its corresponding output text, often used for training or fine-tuning conversational AI models. |

## Google Specific Terms

| Term | Definition |
|------|------------|
| `vertexai` | A Python library used for interacting with Google Cloud's Vertex AI services. It simplifies the process of deploying and using machine learning models. |
| `ChatModel` | A class within the Vertex AI library that represents a conversational AI model. It's used to create chatbots or conversational agents. |
| `from_pretrained` | A method used to load a pre-trained model. This allows users to utilize models that have already been trained on large datasets, saving time and computational resources. |
| `streaming_prediction` | A function or method in AI programming that continuously processes data in real-time, as opposed to batch processing. |
| `project_id` | In cloud services like Vertex AI, it's a unique identifier for a specific project within the cloud platform. |
| `location` | Refers to the geographical location or region of the cloud servers where the AI model is deployed or accessed. |
| `init` | A method used to initialize a setup, in this case, setting up the Vertex AI with project and location details. |
| `send_message_streaming` | A method to send a message to a conversational AI model and receive a response in a streaming fashion, useful for real-time interactions. |

## Database Definitions

| Term | Definition |
|------|------------|
| `SQLite` | A lightweight, disk-based database that doesn't require a separate server process. SQLite is a popular choice for local/client storage in application software. |
| `Cursor` | An object used in databases to execute SQL queries and fetch results. It acts as a pointer to the rows returned by a query, allowing you to read and manipulate the data. |
| `Connection` | A Connection object that represents the database connection. It's used to execute SQL commands and interact with the database. |
| `Table` | In a database, a table is a collection of related data held in a structured format within a database. It consists of rows and columns. |
| `Row` | A single record in a database table, representing a single, implicitly structured data item in a table. |
| `Column` | A set of data values of a particular simple type in a database, one for each row of the table. The column essentially defines the data that can be stored in each row. |


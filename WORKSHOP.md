# Workshop: Create this Project Step-by-Step

## Section 0: Set Up You Google Cloud Account

*Branch `workshop-step-1`*

### Setup in the Cloud

1. Go to google cloud to create an account. You must add a card number to sign up although you will not be billed. You can use a service like privacy.com if you don't want to use a real card number.
2. Look at the project you are using. Something like catdog-dogcat-765432 (My First Project)
3. Get you API keys from google cloud: 
   - https://developers.generativeai.google/tutorials/setup
   - https://makersuite.google.com/u/1/app/apikey
4. Create an object storage bucket in Google cloud

### Setup Locally

1. Set up the project and environment locally by following the Installation instructions in [the README file](README.md).
2. Install dependencies
3. `gcloud auth application-default login`
	1. You will need to download and install the gcp sdk first. Follow the instructions here: https://cloud.google.com/sdk/docs/install
	2. Log in with this in your terminal: ``./bin/gcloud init`
	3. Put it in your path if you want: `export PATH=$PATH:~/google-cloud-sdk/bin`
	4. After successful auth: https://cloud.google.com/sdk/auth_success

## Section 1: Set up the Database

Next, set up the database to store our recipes and ingredients. This will hold crucial information like ingredients, preparation steps, and serving size.

### Schema

Users

- id: INTEGER (Primary Key)
- username: TEXT (Not Null, Unique)
- dietary_restrictions: TEXT
- preferences: TEXT

Active User

- id: INTEGER (Primary Key)
- user_id: INTEGER (Foreign Key referencing Users.id)
- username: TEXT (Not Null)

Ingredients

- id: INTEGER (Primary Key)
- user_id: INTEGER (Foreign Key referencing Users.id)
- name: TEXT (Not Null)
- expiration_date: DATE

Recipes

- id: INTEGER (Primary Key)
- user_id: INTEGER (Foreign Key referencing Users.id)
- name: TEXT (Not Null)
- ingredients: TEXT
- instructions: TEXT

Recipe Ratings

- id: INTEGER (Primary Key)
- recipe_name: TEXT (Not Null)
- rating: INTEGER (Not Null)

## Section 2: Integration with PaLM 2

*Branch `workshop-step-2`*

With our database ready, we'll integrate PaLM 2 to add a layer of basic AI functionality with a single file, `test_google_ai.py`.

## Section 3: Building the MVP of the Recipe Recommendation App

1. Let's ask the user what type of food they want to eat.
2. The AI should respond with 3 recommendations.
3. The user can pick the recipe that they like.
4. The AI will ask the user again and it will repeat.

## Section 4: Making it Pretty

Let's use Pyfiglet and Colorama to spice up our terminal output.

```python
def setup_terminal_ui():
    """Initialize colorama and other terminal UI settings."""

    init(autoreset=True)

    # Display the ASCII header using PyFiglet
    header = pyfiglet.figlet_format("FoodieAIdvisor", font="slant")
    print(Fore.CYAN + header)

    print(
        Fore.GREEN
        + "Welcome to FoodieAIdvisor - Your AI-powered Recipe Advisor!"
    )
    print(Fore.YELLOW + "Enter 'help' anytime to see available commands.\n")
```

## Section 5: Cleaning up the Code

Let's take some time to modularize the code and break things up into separate files.

## Section 6: Adding Users

This is a nice to have feature so it's saved for last!

We created the users and active_users tables at the beginning, but haven't used them yet. Let's add them to our app so you have to select a user when you 

## Section 7: Advanced Features (optional)

- Selecting and Saving Recipes: Once a user selects a recipe, it's automatically saved to our database.
- Recipe Insights: Dive deeper into each recipe to understand nutritional value, origin, and even historical context.
- Measurement Conversion: Switch between metric and imperial systems with ease.

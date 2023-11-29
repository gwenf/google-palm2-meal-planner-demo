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

### Setup in Locally

1. Set up the project and environment locally by following the Installation instructions in [the README file](README.md).
2. install libraries
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

## Section 3: Advanced Feature3.

**Set Up Google Cloud**:
   - Set up a Google Cloud account if you haven't already.
   - Create a new project for your application.
   - Enable the Palm API (or the specific API you intend to use) for the project.
   - Set up the service account and download the JSON key. Ensure you keep this key secure and don't commit it to public repositories.
   - Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the downloaded service account key.

4. **Develop the Terminal UI**: Using `colorama` and `PyFiglet`.

5. **Data Storage with SQLite**: Implement database setup, table creation, and CRUD operations using `sqlite3`.

6. **Backend Logic & AI Integration**:
   - Implement user profile and inventory management.
   - Integrate the Google Palm API for recipe recommendations. Make API calls as necessary based on user input, inventory, and preferences.

- Selecting and Saving Recipes: Once a user selects a recipe, it's automatically saved to our database.
- Recipe Insights: Dive deeper into each recipe to understand nutritional value, origin, and even historical context.
- Measurement Conversion: Switch between metric and imperial systems with ease.

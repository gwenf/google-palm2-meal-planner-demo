# Workshop: Create this Project Step-by-Step

## Section 0: Set Up You Google Cloud Account

### Setup in the Cloud
1. Go to google cloud to create an account. You must add a card number to sign up although you will not be billed. You can use a service like privacy.com if you don't want to use a real card number.
2. Look at the project you are using. Something like catdog-dogcat-765432 (My First Project)
3. Get you API keys from google cloud: 
    - https://developers.generativeai.google/tutorials/setup
    - https://makersuite.google.com/u/1/app/apikey
4. Create an object storage bucket in Google cloud

### Setup in Locally
1. Set up project and environment
2. install libraries
3. `gcloud auth application-default login`
	1. You will need to download and install the gcp sdk first. Follow the instructions here: https://cloud.google.com/sdk/docs/install
	2. Login with this: ``./bin/gcloud init`
	3. Put it in your path if you want: `export PATH=$PATH:~/google-cloud-sdk/bin`
	4. After successful auth: https://cloud.google.com/sdk/auth_success

## Section 1: Set up the Database

1. Set up the app locally by following the instructions in [README.md](README.md)
2. Next, set up the database to store our recipes and ingredients. This will hold crucial information like ingredients, preparation steps, and serving size.

## Section 2: Integration with PaLM 2

With our database ready, we'll integrate PaLM 2 to add a layer of AI functionality. This includes:

- Selecting and Saving Recipes: Once a user selects a recipe, it's automatically saved to our database.
- Recipe Insights: Dive deeper into each recipe to understand nutritional value, origin, and even historical context.
- Measurement Conversion: Switch between metric and imperial systems with ease.

## Section 3: Advanced Features

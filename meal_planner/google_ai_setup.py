from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project="my-project",
    # the Vertex AI region you will use
    # defaults to us-central1
    location="us-central1",
    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    # TODO:
    staging_bucket="gs://chat-bison-objects-2",
    # custom google.auth.credentials.Credentials
    # environment default credentials used if not set
    # NOTE: I'm using defaults
    # credentials=my_credentials,
    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    # NOTE: skipping
    # encryption_spec_key_name=my_encryption_key_name,
    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment="meal_planner_experiment",
    # description of the experiment above
    experiment_description="A smart AI-powered meal planner.",
)

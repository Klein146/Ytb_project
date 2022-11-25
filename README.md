# GET COMMENTS WITH THE YOUTUBE API

We create a data pipeline
from the youtube api we get the comments of a specific video,
Then, we will use an orchestrator (Airflow) that allows us to establish the connection with the database (Postgres) that stores our dataframe and executes the queries 
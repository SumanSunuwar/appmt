from fastapi import FastAPI
from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:tqyQCShrlNflEfCdItDubMpS:e044b74ca88ac5f564dea4188dd557df3f891e82453c55ea99b9e125f94f9f3f")
db = client.get_database_by_api_endpoint(
  "https://b4871b2b-6154-4952-ab6e-889c819fac4c-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

# app = FastAPI()


# @app.get("/")
# def homepage():
#     return {"hello": "world"}
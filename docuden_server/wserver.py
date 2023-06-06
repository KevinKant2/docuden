import weaviate
from dotenv import load_dotenv
import os

load_dotenv()



client = weaviate.Client(
    url="http://localhost:8080/",
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAIKEY"),
    })

client.schema.get()


import pymongo
import openai
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

MODEL="text-embedding-ada-002"

openai.api_key = OPEN_AI_KEY

def createEmbedding(input):
    response = openai.Embedding.create(engine=MODEL, input=input)
    return (response.data[0].embedding)


connection = pymongo.MongoClient("mongodb://localhost:27017/")
db  = connection["the_brain"]

embeddings = db["embeddings"]

woord = "tappie"

if embeddings.find_one({ "name": woord }):
    print(woord + " already exists in the database")
    data =1 
else: data = {"name": woord, "embedding": createEmbedding(woord)} 


if data != 1:
    print("inserting " + woord + " into the database")
    embeddings.insert_one(data)

    







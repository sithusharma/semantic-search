import os
import openai
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("spotify-songs")

def embed_text(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def retrieve_best_matches(query):
    query_embedding = embed_text(query)
    results = index.query(vector=query_embedding, top_k=5, include_metadata=True)

    matched_chunks = [match['metadata']['description'] for match in results['matches']]

    return "Here are the top matching songs:\n\n" + "\n\n".join(matched_chunks)

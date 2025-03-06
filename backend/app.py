from fastapi import FastAPI
from retrieval_service import retrieve_best_matches

app = FastAPI()

@app.get("/search")
def search_song(query: str):
    response = retrieve_best_matches(query)
    return {"response": response}

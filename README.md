# Music Search Platform - Demo Version

This repository contains a **demo version** of a music search platform.  
The original version was built as part of a **company project** and used **different technology and infrastructure**.  
Due to company rules, the actual codebase (frontend, backend, and pipelines) is **private** — this repo only includes a simplified example to show the **preprocessing and basic search logic**.

---

## What the Original System Did
The original project was made to **help users search for songs using natural language**.  
Example:  
> "Find upbeat pop songs from 2023"

The system would find songs that matched the **feeling** of the query — even if the song name or artist didn’t contain those exact words.

---

##  Tech Stack (Original vs Demo)

| Layer               | Original Tech (Company)     | Demo Tech (Here)   |
|----------------|------------------|------------------|
| Frontend         | Angular          | Streamlit |
| Backend - Main API | Node.js           | FastAPI |
| Backend - Processing | Flask               | FastAPI (combined) |
| Vector Database  | Azure CosmosDB | Pinecone |
| Embedding Model | Azure OpenAI   | Azure OpenAI |

---

## Data Used
Both versions (original and demo) used **Spotify song data**, including:
- Track name and artist(s)
- Release date
- Audio features (danceability, energy, tempo, etc.)

---

## What This Demo Code Does
This demo includes a **data processing script** (`preprocess.py`) that:
1. Reads a Spotify songs **CSV file**.
2. Combines useful data into short **descriptions** for each song.
3. Converts those descriptions into **embeddings** using Azure OpenAI’s embedding model.
4. Uploads those embeddings into **Pinecone**, a vector search database.

---

## Search Flow (in the Original and Demo Versions)
| Step | What Happens |
|----|----|
| 1 | User types a search like "chill indie songs from 2020" |
| 2 | Query is cleaned and embedded using Azure OpenAI |
| 3 | Embedding is compared to all song vectors in Pinecone |
| 4 | Closest matches (most similar songs) are returned |
| 5 | Frontend displays the matching songs |

---

## Why Vector Search?
Traditional search only finds **exact word matches**.  
Vector search finds **songs with similar meaning**.  
For example, searching for "summer road trip songs" might return:
- "Highway Vibes" (even though "summer" isn’t in the title)
- "Beach Drive" (because it understands the **feeling**, not just the words)

---

## Files Included
| File                  | What It Does |
|----------------|------------------|
| `preprocess.py`    | Prepares and uploads data to Pinecone |
| `search_service.py` | Runs a basic search API |
| `.env.example`      | Template for your API keys |
| `app.py`              | Simple Streamlit frontend for testing search |

---

##  How to Run (Demo Version)
1. Place your Spotify dataset CSV into `data/spotify_songs.csv`
2. Add your `PINECONE_API_KEY` and `OPENAI_API_KEY` to `.env`
3. Preprocess the data:
    ```bash
    python preprocess.py
    ```
4. Start the search backend:
    ```bash
    uvicorn search_service:app --reload
    ```
5. Start the frontend:
    ```bash
    streamlit run app.py
    ```

---

##  Note
This demo version is simplified for open sharing.  
The **real system** at the company used:
- Azure CosmosDB for vector search
- Azure Bot Framework for chatbot logic
- Azure Cognitive Search for advanced filters
- Node.js and Flask for more scalable backend pipelines

That code is **private** and cannot be included here.



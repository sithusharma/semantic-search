

# 🎵 Music Search Platform 

The code in this repository is a demo of what the front and back end would look like with third party services (Streamlit, Render, PineconeDB)

This project was built as part of a company project to make a **smart music search tool**. The goal was to let users type in a natural language search like "upbeat pop songs from 2023" and get **relevant songs** — even if the song titles didn’t exactly match the words they typed.

---

## ⚙️ Tech Stack

| Part               | What we used |
|-------------------|----------------|
| Frontend         | Angular |
| Backend - Main API | Node.js |
| Backend - Data Processing | Flask |
| Vector Database  | Azure CosmosDB (with vector search enabled) |
| Embedding Model | Azure OpenAI (text-embedding-ada-002) |

---

## 📥 Data Pipeline - How We Prepped the Data

### Where the Data Came From
The data we used was **Spotify song data**, which had things like:
- Song name and artist
- Release date
- Danceability, energy, tempo, and other audio features

This was originally provided in a **CSV file**.

---

### What the Preprocessing Did
We used a **Jupyter Notebook (`cosmos.ipynb`)** to:

1. Read the CSV file and clean up the data.
2. Combine all useful info about each song into a **text summary** (like “This is a happy dance song by Drake from 2022”).
3. Convert those summaries into **vectors (embeddings)** using **Azure OpenAI’s embedding model**.
4. Store the vectors along with song metadata in **CosmosDB**, which supports **vector search**.

---

### Storage
All the preprocessed song data — including the embeddings and song details — was saved to **Azure CosmosDB**. CosmosDB was set up to do **vector similarity search** so it could find songs that were closest in meaning to the search query.

---

## 🌐 How the Whole System Worked
- The **frontend (Angular)** gave users a search bar where they could type something like "relaxing indie songs from 2019."
- The **main backend (Node.js)** received the search and forwarded it to a smaller **Flask service**.
- The Flask service took the query, cleaned it up, and turned it into a vector using the same OpenAI embedding model.
- That vector was passed to **CosmosDB**, which ran the actual vector search.
- CosmosDB returned the closest matching songs, and the backend sent them back to the frontend to display.

---

## 📊 About the Notebook (`cosmos.ipynb`)
Because this was part of a **company project**, I can’t share the actual **Angular frontend, Node backend, or Flask code**.

However, the **notebook (`cosmos.ipynb`)** is included to show:

- How the data got cleaned up.
- How the embeddings were generated using Azure OpenAI.
- How the song data (vectors + metadata) got uploaded into CosmosDB.

At the bottom of the notebook, there’s also an **example query** showing CosmosDB returning songs based on a sample search. This helps demonstrate that the system works — you can see how the search vector pulls back relevant songs based on meaning, not just exact words.

---

## 🚀 Why Use Vector Search?
Normal search (like `track_name LIKE '%love%'`) only works if the exact words match. By using vectors, the system could find songs that **feel similar** to the search query — even if none of the exact words were in the song name. For example, a search for "chill beach music" could still find a song called "Ocean Vibes" — even though "chill" and "beach" aren’t in the title.

---

## 🔒 Important Note
This project was made for a company, so only the preprocessing notebook is included here. Everything else (the actual app code) is kept private.

# 🎵 Intelligent Music Search Platform

This project was developed as part of a company initiative to create an **intelligent music retrieval platform** capable of understanding **natural language queries** and returning the most relevant songs. The system leverages a **combination of frontend, backend, vector search, and AI-powered embeddings** to enable **semantic music search** across a large catalog of songs.

---

## ⚙️ Tech Stack

| Layer               | Technology |
|-------------------|----------------|
| Frontend         | Angular |
| Backend - API Gateway | Node.js |
| Backend - Data Processing | Flask |
| Vector Database  | Azure CosmosDB (Vector Search) |
| Embedding Model | Azure OpenAI (text-embedding-ada-002) |

---

## 📥 Data Pipeline - Preprocessing & Storage

### Data Source
The dataset used for this project consisted of **Spotify song metadata**, including attributes like track name, artists, release date, and audio features such as danceability, energy, and tempo. This data was initially provided as a **CSV file**.

---

### Data Preprocessing
A **Jupyter Notebook (`cosmos.ipynb`)** was created to handle:

- Reading and cleaning the Spotify data.
- Transforming each song’s metadata into a **text description** to capture meaningful context (track name, artist, release date, and attributes like danceability and energy).
- Converting these text descriptions into **vector embeddings** using **Azure OpenAI’s `text-embedding-ada-002`** model.
- Preparing each document with both:
    - The **embedding vector** (for semantic search).
    - **Metadata** (track name, artist name, year, etc.) to support filtering and display.

---

### Storage
The preprocessed song data (embeddings + metadata) was stored in **Azure CosmosDB** using its **native vector search capability**. CosmosDB was configured to support **vector similarity search** (cosine distance) on the embeddings, enabling semantic music retrieval.

---

## 🌐 System Architecture
- The **frontend (Angular)** provided the user interface, allowing users to enter natural language queries such as "upbeat pop songs from 2023".
- The **backend (Node.js)** served as the main API gateway, handling incoming requests from the frontend.
- The **data processing backend (Flask)** was responsible for:
    - Query pre-processing (cleaning and enriching the query).
    - Converting user queries into **embedding vectors** using **Azure OpenAI**.
    - Executing **vector similarity search** against **CosmosDB**.
    - Returning the matched songs with their metadata to the frontend.

---

## 📊 Notebook (`cosmos.ipynb`)
Since this project was developed as part of a **company project**, the majority of the production code (Angular frontend, Node.js gateway, and Flask processing service) **cannot be shared publicly**.

However, the **data preprocessing notebook (`cosmos.ipynb`)** is provided to demonstrate:

- Data cleaning.
- Embedding generation using Azure OpenAI.
- Vector document construction.
- Bulk upload to CosmosDB.

This notebook serves as a standalone demonstration of the **data preparation process**.

---

## 🚀 Why Vector Search?
Traditional keyword search (like `track_name LIKE '%love%'`) is **limited** to exact matches. By converting each song into a **semantic embedding vector**, the system could:
- Understand that "happy dance music" relates to **high danceability and positive valence tracks**.
- Retrieve songs that match the **intent** behind the query, not just the literal words.

---

## 🔒 Company Disclaimer
This project was part of proprietary development for a corporate client, and only the **preprocessing notebook** is visible in this repository. The **full project (frontend, API gateway, and Flask processing backend)** remains private due to **intellectual property restrictions**.

---

## 📂 Repository Structure

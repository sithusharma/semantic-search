import pandas as pd
import openai
import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("✅ Environment variables loaded.")

# Init Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "spotify-songs"
if index_name not in pc.list_indexes().names():
    print(f"⚙️ Creating index '{index_name}'...")
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
else:
    print(f"✅ Index '{index_name}' already exists.")

index = pc.Index(index_name)

# Load dataset
csv_path = "../data/spotify_songs.csv"
print(f"📥 Loading dataset from {csv_path}")
df = pd.read_csv(csv_path)

# Setup OpenAI
openai.api_key = OPENAI_API_KEY

def embed_text(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

# Attributes to vectorize separately
attribute_templates = {
    "track_name": "Track name: {value}",
    "artist_name": "Artist: {value}",
    "release_date": "Released in {value}",
    "bpm": "This song has a tempo of {value} BPM",
    "key": "Key: {value}",
    "mode": "Mode: {value}",
    "danceability": "Danceability: {value}%",
    "energy": "Energy: {value}%",
    "valence": "Valence (mood): {value}%",
    "acousticness": "Acousticness: {value}%",
    "liveness": "Liveness: {value}%",
    "speechiness": "Speechiness: {value}%"
}

# Prepare all vectors
vectors = []

for i, row in df.iterrows():
    track_id = str(i)

    for attr, template in attribute_templates.items():
        value = row[attr] if attr in row else row.get(f"{attr}_%")  # Handle percentages
        if pd.isna(value):
            continue

        description = template.format(value=value)
        embedding = embed_text(description)

        vectors.append({
            "id": f"{track_id}-{attr}",
            "values": embedding,
            "metadata": {
                "track_id": track_id,
                "attribute": attr,
                "text": description
            }
        })

    if i % 50 == 0:
        print(f"✅ Processed {i+1}/{len(df)} songs")

# Batch upload to Pinecone (handle 4MB limit)
BATCH_SIZE = 100

print(f"⬆️ Uploading vectors to Pinecone in batches of {BATCH_SIZE}...")

for i in range(0, len(vectors), BATCH_SIZE):
    batch = vectors[i:i+BATCH_SIZE]
    index.upsert(batch)
    print(f"✅ Uploaded batch {i//BATCH_SIZE+1}/{(len(vectors) + BATCH_SIZE - 1) // BATCH_SIZE}")

print("✅ Data successfully uploaded to Pinecone!")

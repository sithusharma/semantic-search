import streamlit as st
import requests

st.title("🎶 Spotify Song Search")

st.write("This is a demo that lets you find songs by describing them.")

query = st.text_input("Describe the song you're looking for:")

if st.button("Search"):
    with st.spinner("Searching in the database..."):
        response = requests.get("http://localhost:8000/search", params={"query": query})
        if response.status_code == 200:
            st.write("### Results:")
            st.write(response.json()["response"])
        else:
            st.error(f"Failed to contact backend. Error: {response.status_code}")

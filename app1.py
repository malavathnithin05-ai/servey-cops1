import streamlit as st
import requests

st.title("👗 Generative AI Fashion Recommender")

gender = st.selectbox(
    "Select Gender",
    ["Male","Female","Unisex"]
)

occasion = st.selectbox(
    "Occasion",
    ["Casual","Party","Office","Wedding"]
)

season = st.selectbox(
    "Season",
    ["Summer","Winter","Spring","Autumn"]
)

color = st.text_input("Preferred Color")

if st.button("Generate Outfit"):

    response = requests.post(
        "http://127.0.0.1:8000/recommend",
        json={
            "gender": gender,
            "occasion": occasion,
            "season": season,
            "color_preference": color
        }
    )

    result = response.json()

    st.subheader("✨ AI Suggested Outfit")

    st.write(result["recommendation"])
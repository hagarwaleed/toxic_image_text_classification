import streamlit as st
from app.controllers.prediction_controller import (
    predict_from_text,
    predict_from_image
)
from app.database.db import init_db
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #DBD9D9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize DB
init_db()

st.markdown(
    """
    <h1 style='text-align: center; font-weight: bold; margin-bottom: 40px;'>
        Toxic Image & Text Classifier
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='font-size:26px;'>Choose Input Type:</h3>",
    unsafe_allow_html=True
)

option = st.radio("", ("Text", "Image"))

st.markdown("<br>", unsafe_allow_html=True)

if option == "Text":

    st.markdown(
        "<h3 style='font-size:28px; margin-top:40px;'>Enter your text:</h3>",
        unsafe_allow_html=True
    )

    text_input = st.text_area("", height=150)

    if st.button("Predict"):
        if text_input.strip() != "":
            label = predict_from_text(text_input)
            st.success(f"Predicted Toxic Category: {label}")
        else:
            st.warning("Please enter some text.")

elif option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            caption, label = predict_from_image(uploaded_file)

            st.info(f"Generated Caption: {caption}")
            st.success(f"Predicted Toxic Category: {label}")
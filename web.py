import streamlit as st
import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import pickle

# Set the page title and icon
st.set_page_config(
    page_title="MaveliKingdom",
    page_icon="👑",
    layout="wide"
)

# Add a background image with 50% transparency
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/onam-maveli-character-3d-render-imagejpg_661323-66.jpg?w=2000');
        background-size: cover;
        background-blur: 75px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load intents data
with open("intents.json") as file:
    data = json.load(file)

def get_chatbot_response(user_input):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([user_input]),
                                         truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])

# Add a navbar
st.sidebar.title("MaveliKingdom")
selected_page = st.sidebar.radio("Navigation", ["Home", "About Us"])
if selected_page == "Home":
    st.write("Welcome to MaveliKingdom! We are here to assist you with your queries.")

# Main content
st.title("MaveliKingdom Chatbot")
st.subheader("Ask your questions below:")

# Transparent text area using CSS
st.markdown(
    """
    <style>
    textarea {
        background-color: rgba(255, 255, 255, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

user_input = st.text_area("User Input:")

if st.button("Submit"):
    bot_response = get_chatbot_response(user_input)
    st.text_area("Bot Response:", bot_response, disabled=True)

# "About Us" section
if selected_page == "About Us":
    st.write("## About Us\n\nMaveliKingdom is a place of rich cultural heritage and tradition. "
             "We celebrate the spirit of Maveli, the legendary king, and the festival of Onam. "
             "Here are some reliable sites to learn more about Maveli and Onam:")

    # Links to reliable sites
    st.markdown("- [Wikipedia - Maveli](https://en.wikipedia.org/wiki/Mahabali)")
    st.markdown("- [Wikipedia - Onam](https://en.wikipedia.org/wiki/Onam)")
    st.markdown("- [Kerala Tourism](https://www.keralatourism.org/onam/)")
    st.markdown("- [History of Onam](https://www.historyofonam.com/)")

# Footer
st.sidebar.markdown("© 2023 A&A")

# Set the color theme to "floral"
st.markdown(
    """
    <style>
    body {
        background-color: #F9EBEA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

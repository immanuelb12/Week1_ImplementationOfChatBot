import nltk
import random
import os
import ssl
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.chat.util import Chat, reflections

# Simple chatbot logic
pairs = [
    ['my name is (.*)', ['Hello %1, how can I help you today?']],
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Greetings!']],
    ['(.*) your name?', ['I am a chatbot created to assist you.']],
    ['(.*) help (.*)', ['I can help you with your queries.']],
    ['(.*) (location|city) ?', ['I am not sure about locations.']],
    ['(.*) (created|made) ?', ['I was created by a developer.']],
    ['(.*) (fine|good|well)', ['Glad to hear that!']],
    ['what is your purpose?', ['I am here to chat with you and provide assistance.']],
    ['tell me a joke', ['Why did the scarecrow win an award? Because he was outstanding in his field!']],
    ['(.*) (weather|forecast) ?', ['I am not sure about the weather, but I hope it’s nice!']],
    ['(.*)', ['I am sorry, I do not understand.']]
]

def chatbot():
    st.title("Simple Chatbot")
    while True:
        user_input = st.text_input("You: ")
        if user_input.lower() == "quit":
            break
        if user_input:
            chat = Chat(pairs, reflections)
            response = chat.respond(user_input)
            st.text(f"Chatbot: {response}")


def chatbot():
    st.title("Simple Chatbot")
    user_input = st.text_input("You: ")
    if user_input:
        chat = Chat(pairs, reflections)
        response = chat.respond(user_input)
        st.text(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()

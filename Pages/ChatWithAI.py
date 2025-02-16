import streamlit as st
import openai
import os

st.title("Chat with Mobo")
user_chat = st.text_area("Ask or Tell Mobo something:", "")

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(user_chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_chat}]
    )
    return response["choices"][0]["message"]["content"]

if st.button("Send"):
    if user_chat.strip():
        response = get_gpt_response(user_chat)
        st.write("Mobo's Response:", response)
    else:
        st.warning("Please enter a message to chat with Mobo.")
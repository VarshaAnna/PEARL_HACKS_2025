import streamlit as st                  # Streamlit
from textblob import TextBlob
import openai                           # OpenAI AI's models GPT-3
import os
import random

st.set_page_config(page_title="MindEase", page_icon="🧠", layout="centered", initial_sidebar_state="expanded")
st.title("MindEase")

# Sidebar
st.sidebar.title("MindEase")
st.sidebar.write("Select to view the Mood History.")

# Main
user_input = st.text_area("Write to us about how you feel today:"," ")


if "moodhistory" not in st.session_state:
    st.session_state.moodhistory = []

openai.api_key = os.getenv("OPENAI_API_KEY")
def get_gpt_response(user_input):
    response = openai.ChatCompletion.create(
        model ="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

if st.button("Analyze Mood"):
    if user_input:
        sentiment_score = TextBlob(user_input).sentiment.polarity
        st.session_state.moodhistory.append(sentiment_score)

        positive_advice = [
            "That's awesome! Keep up the positive energy and Keep smiling.",
            "Fantastic! Keep up the good work and continue doing what makes you happy.",
            "Wonderful! Stay motivated and enjoy every moment of your day."
        ]

        negative_advice = [
            "It's okay to not be okay. Give yourself permission to feel your emotions without judgment. Acknowledge them, but don’t let them define you. You're stronger than you think.",
            "You don’t have to go through this alone. Talk to a trusted friend, family member, or professional. Sometimes, sharing your thoughts can lighten the burden more than you expect.",
            "Be kind to yourself. You’re doing the best you can, and that’s enough. Avoid negative self-talk and remind yourself that you deserve care and understanding.",
            "If you're feeling overwhelmed, break your day into small, manageable steps. Even completing a simple task, like drinking water or taking a deep breath, can help you regain a sense of control.",
            "Try focusing on something small that brings you comfort—a favorite song, a warm drink, or a cozy blanket. Even small joys can provide relief when things feel difficult.",
            "Take a moment for yourself. A short walk, deep breathing, journaling, or listening to music can help you reconnect with yourself and create space for healing."
        ]

        neutral_advice = [
            "Sometimes, a neutral mood is a chance to do something enjoyable without pressure. Listen to your favorite music, read a book, or go for a short walk to refresh your mind.",
            "A neutral state can be a great time to focus on balance—physically, emotionally, and mentally. Stay hydrated, move a little, and check in with your thoughts.",
            "A neutral mood is perfect for creativity. Try journaling, drawing, or even just jotting down your thoughts. You never know what inspiration might strike!",
            "Even if you're not feeling overly happy or sad, mindfulness can help you stay grounded. Take a few deep breaths, focus on the present moment, and appreciate where you are.",
            "Feeling neutral? Use this moment to set yourself up for success. Organize your space, plan your week, or check off a small task—it’ll make your future self grateful!"
        ]
        if sentiment_score > 0:
            mood = "😊 Positive"
            advice = random.choice(positive_advice)
        elif sentiment_score < 0:
            mood = "😟 Negative"
            advice = random.choice(negative_advice)
        else:
            mood = "😐 Neutral"
            advice = random.choice(neutral_advice)

        st.write(f"**Mood Detected:** {mood}")
        st.write(f"**Advice:** {advice}")

gif_urls = [
    "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",  
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW84Ynloc3E4czFobnc0cGpyZnEzazV2MDJjbnMxeDlpZmdzbG1sdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ta2eHM043vhVS/giphy.gif",
    "https://media.giphy.com/media/kT1XesVhXxEOFMs7j2/giphy.gif?cid=ecf05e475mpsao3xswlwehoxzw4w9y1c5sg5wucpea7os1um&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/zZMTVkTeEfeEg/giphy.gif?cid=790b76112i7f52q119gg073uddht5v8pzjgwhuzl7f0j9h7v&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif?cid=790b76112i7f52q119gg073uddht5v8pzjgwhuzl7f0j9h7v&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif?cid=790b7611ib69ik482bstm5i05flc0x8xy0pi2vokeghr41vm&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/q9ETKoMaBMsNy/giphy.gif?cid=ecf05e47tuarz2y3ocz07tqf4nuhwifo6vr2amnpm5in3pzo&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif?cid=790b7611qu1ofmtw2fb1s1tgf5e1r5kj15rczioeek01afsv&ep=v1_gifs_search&rid=giphy.gif&ct=g"
]      
gif = random.choice(gif_urls)
st.image(gif, width=400, caption="Stay pawsitive! You got this!")      # use_container_width=True

if st.button("Talk to Mobo"):
    if user_input:
        response = get_gpt_response(user_input)
        st.write("💬 **Mobo's Response:**", response)
    else:
        st.warning("Please enter a message to chat with Mobo.")

import streamlit as st
import matplotlib.pyplot as plt

st.title("Mood History Over Time")

if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

if len(st.session_state.mood_history) > 0:
    st.write("Here's how your mood has changed over time based on your input:")
       # Plot Mood History
    plt.figure(figsize=(8, 4))
    plt.plot(st.session_state.mood_history, marker='o', linestyle='-', color='b')
    plt.xlabel("Entries")
    plt.ylabel("Mood Score")
    plt.title("Mood Trends Over Time")
    plt.grid(True)

    st.pyplot(plt)
else:
    st.warning("No mood data available yet. Try analyzing your mood first on the main page!")


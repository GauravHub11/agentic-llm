import streamlit as st
from src.agent import run_agent

st.title("Agentic AI System")
st.write("Interact with the AI agent for various tasks like summarization, sentiment analysis, entity extraction, code generation, and translation.")

# User input
user_input = st.text_area("Enter your query:")

if st.button("Run Agent"):
    if user_input.strip():
        response = run_agent(user_input)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter a valid query.")

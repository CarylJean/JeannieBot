import streamlit as st
import random
import time
import pandas as pd

st.title("Jeannie Chat Bot")

# Load questions and answers from a CSV file on GitHub
csv_url = "https://raw.githubusercontent.com/your-username/your-repo/master/data.csv"
questions_and_answers = pd.read_csv(csv_url)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Select a random question and answer pair from the CSV file
    random_row = questions_and_answers.sample(n=1)
    question = random_row["Question"].values[0]
    answer = random_row["Answer"].values[0]

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate typing the question
        for chunk in question.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
        time.sleep(1)  # Add a brief pause
        
        # Simulate typing the answer
        full_response = ""
        for chunk in answer.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": f"Question: {question}\nAnswer: {answer}"})

import streamlit as st
import google.generativeai as palm

palm.configure(api_key="AIzaSyBdY9bOtYv0M_-xdj6gJShZfqjpuCjE92U")

def initiate(user_input):
    prompt = f"""
    Analyzing Car Issues:
    User Input: {user_input}
    """

    response = palm.chat(messages=prompt)
    return response

def reply(prev_msg, user_input):
    prompt = f"""
    Previous AI Response: {prev_msg.last}
    User Input: {user_input}
    """

    return prev_msg.reply(prompt)

def ai_car_diagnosis():
    st.title("AI Car Diagnosis")

    # Initial interaction
    user_input = st.text_input("User:", key="initial_input")
    response = initiate(user_input)
    st.text(f"AI: {response.last}")

    # Continuing the conversation
    i = 1
    while True:
        user_input = st.text_input(f"User {i}:", key=f"user_input_{i}")
        i += 1

        if user_input.lower() in ["exit", "quit", "stop"]:
            st.text("Exiting AI Car Diagnosis.")
            break

        response = reply(response, user_input)
        st.text(f"AI: {response.last}")

#if __name__ == "__main__":
#    ai_car_diagnosis()
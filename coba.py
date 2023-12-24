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
    user_input = st.text_input("User:")
    response = initiate(user_input)
    st.text(f"AI: {response.last}")

    # Continuing the conversation
    with st.form("user_inputs_form"):
        user_input_list = [user_input]
        while st.form_submit_button("Submit") and user_input.lower() not in ["exit", "quit", "stop"]:
            user_input = st.text_input("User:")
            user_input_list.append(user_input)
            response = reply(response, user_input)
            st.text(f"AI: {response.last}")

    st.text("Exiting AI Car Diagnosis.")

if __name__ == "__main__":
    ai_car_diagnosis()

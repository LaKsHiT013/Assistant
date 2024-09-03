import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def show():
    st.title("Ask Me Anything!")
    
    # Display header and input text
    st.header("Drop your query!")
    user_input = st.text_area("Question:", key="input", placeholder="Command...")
    
    # Add a submit button
    submit_button = st.button("Submit")
    
    # Display a spinner while processing
    with st.spinner('Let Me Think...'):
        if submit_button:
            if user_input:
                try:
                    # Initialize model and generate response
                    model = genai.GenerativeModel('gemini-1.0-pro-latest')
                    response = model.generate_content(user_input)
                    
                    # Display response
                    st.subheader("I got it:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("You haven't asked anything.")
    
    # Optionally, add more interactive elements
    st.sidebar.header("Settings")
    st.sidebar.text("Adjust model parameters or choose different models here.")

if __name__ == "__main__":
    show()

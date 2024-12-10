import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import threading
import comtypes
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

recognizer = sr.Recognizer()
tts_lock = threading.Lock()

def initialize_engine():
    comtypes.CoInitialize() 
    return pyttsx3.init()


engine = initialize_engine()


def listen_to_speech():
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Recognized speech: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            st.write("Sorry, there was a request error with the API.")
            return None


def generate_llm_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.write(f"Error in generating response: {e}")
        return None


def speak_text(text):
    def run_tts():
        while True:
            with tts_lock: 
                engine.stop() 
                engine.say(text)
                engine.runAndWait()


    tts_thread = threading.Thread(target=run_tts)
    tts_thread.start()

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

st.title("Speech-to-Speech LLM Bot")

if st.button("Start Conversation"):
    input_text = listen_to_speech()

    if input_text:
        st.session_state.conversation_history.append(f"You: {input_text}")
        response = generate_llm_response(input_text)

        if response:
            st.session_state.conversation_history.append(f"Bot: {response}")
            speak_text(response)  

    for msg in st.session_state.conversation_history:
        st.write(msg)

if st.button("Reset Conversation"):
    st.session_state.conversation_history = []
    st.write("Conversation reset.")

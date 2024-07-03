# app.py
import streamlit as st
from tts_function import text_to_speech

# Streamlit app
st.title("Text to Speech Converter")

# Input text from user
text = st.text_area("Enter the text you want to convert to audio:")

# Language selection
language = st.selectbox("Select the language", ["en"])

# Button to generate audio
if st.button("Convert to Speech"):
    if text:
        # Convert text to speech
        filename = text_to_speech(text, language)
        
        # Indicate that the audio is generated
        st.success("Audio generated successfully!")

        # Provide a way to download the audio file
        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
            st.download_button("Download audio file", data=audio_bytes, file_name=filename, mime="audio/mp3")
    else:
        st.error("Please enter some text to convert to speech.")

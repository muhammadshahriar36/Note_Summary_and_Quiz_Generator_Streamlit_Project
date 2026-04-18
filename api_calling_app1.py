from google import genai
import os, io
from dotenv import load_dotenv
import streamlit as st 
from gtts import gTTS


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

# print(response.text)

# st.markdown(response.text)

def note_generator(pil_images):
    prompt = "Summarize the pictures in note formate at max 100 words, make sure to add necessary markdown to differentiate different section"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt],
        )
    return response.text
    
    
    
def audio_transcription(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer
    
    
    
def quiz_generator(image,difficulty):
    prompt = f"Generate 3 quizzes based on the{difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too, after the quiz"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt],
        )
    return response.text
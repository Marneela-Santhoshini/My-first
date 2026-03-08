
import speech_recognition as sr
from gtts import gTTS
import os
from langchain_openai import ChatOpenAI

# Set API key
os.environ["OPENAI_API_KEY"] = "sk-12345678"
# Speech recognition
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio)

print("Original:", text)

from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-es"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

inputs = tokenizer(text, return_tensors="pt", padding=True)
translated = model.generate(**inputs)

translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

print("Translated:", translated_text)

# Text to speech
tts = gTTS(text=translated_text, lang="es")
tts.save("translated.mp3")

os.system("start translated.mp3")
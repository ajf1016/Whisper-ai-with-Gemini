import whisper
import ssl
import google.generativeai as genai
import os
GOOGLE_API_KEY = 'your key'
ssl._create_default_https_context = ssl._create_unverified_context
genai.configure(api_key=GOOGLE_API_KEY)
model = whisper.load_model("base")
result = model.transcribe("03.mp3")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Summarize this text" + result["text"])
print(response.text)
print("+======================================================+")
print(result["text"])

with open("response.txt", "w") as response_file:
    response_file.write(response.text)

with open("original_text.txt", "w") as original_text_file:
    original_text_file.write(result["text"])

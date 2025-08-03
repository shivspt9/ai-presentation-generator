import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

app = FastAPI()

# Pydantic model for input
class Prompt(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "AI Presentation Generator is running."}

@app.post("/generate")
def generate_text(prompt: Prompt):
    try:
        response = model.generate_content(prompt.message)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

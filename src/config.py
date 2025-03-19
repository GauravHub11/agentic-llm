import os
from dotenv import load_dotenv

load_dotenv()

# API Key for Gemini
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Please set it in .env")

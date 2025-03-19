import os
from dotenv import load_dotenv

load_dotenv()

# API Key for Gemini
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Please set it in .env")

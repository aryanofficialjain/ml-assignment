# config.py
import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyB9gxkuMMuIt_9C4ox3fxU0OcmfLmPsWwU")

# Model Settings
MODEL = "gemini-2.0-flash"
TEMPERATURE = 0

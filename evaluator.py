# evaluator.py
from google import genai
from google.genai import types
from prompts import build_prompt
from config import GEMINI_API_KEY, MODEL, TEMPERATURE
from utils import safe_parse

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

def evaluate_answer(question, answer, rubric):
    """
    Evaluates a student's answer using a provided rubric.
    """
    prompt = build_prompt(question, answer, rubric)
    
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE,
                response_mime_type="application/json",
            )
        )
        output = response.text
        return safe_parse(output)
    except Exception as e:
        return {"error": str(e)}

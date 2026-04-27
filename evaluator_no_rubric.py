# evaluator_no_rubric.py
from google import genai
from google.genai import types
from prompts_no_rubric import build_prompt_no_rubric
from config import GEMINI_API_KEY, MODEL, TEMPERATURE
from utils import safe_parse

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

def evaluate_no_rubric(question, answer):
    """
    Evaluates a student's answer without a specific rubric.
    """
    prompt = build_prompt_no_rubric(question, answer)
    
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

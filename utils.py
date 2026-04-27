# utils.py
import json
import re

def safe_parse(output):
    """
    Safely parses JSON from LLM output, handling markdown blocks if present.
    """
    try:
        # Try direct parse
        return json.loads(output)
    except json.JSONDecodeError:
        # Try to extract JSON from markdown blocks
        json_match = re.search(r'```json\n(.*?)\n```', output, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass
        
        # Try to find anything that looks like a JSON object
        json_match = re.search(r'({.*})', output, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass
        
        return {
            "error": "Parsing failed",
            "raw_output": output
        }

def validate_input(question, answer):
    """
    Basic validation for input fields.
    """
    if not question.strip():
        return False, "Question cannot be empty."
    if not answer.strip():
        return False, "Answer cannot be empty."
    if len(answer.strip()) < 5:
        return False, "Answer is too short to be evaluated fairly."
    return True, ""

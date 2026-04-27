# prompts_no_rubric.py

def build_prompt_no_rubric(question, answer):
    return f"""
Evaluate the following student answer.

Question:
{question}

Answer:
{answer}

Give marks out of 5 based on general correctness and clarity.

Return ONLY JSON:
{{
  "marks_awarded": float,
  "max_marks": 5,
  "feedback": "clear feedback",
  "justification": "reasoning"
}}
"""

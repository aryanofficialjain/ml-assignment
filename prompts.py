# prompts.py

def build_prompt(question, answer, rubric):
    return f"""
You are a strict teacher.
Evaluate the student's answer ONLY based on the provided rubric.

Question:
{question}

Student Answer:
{answer}

Rubric:
{rubric}

Rules:
- Follow the rubric strictly.
- Do not assume knowledge not present in the answer.
- Award marks strictly based on rubric criteria.
- Deduct marks if parts are missing.

Return ONLY JSON:
{{
  "marks_awarded": float,
  "max_marks": {rubric['max_marks']},
  "feedback": "clear feedback",
  "justification": "reasoning"
}}
"""

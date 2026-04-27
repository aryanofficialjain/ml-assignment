# rubrics.py
physics_rubric = {
    "subject": "physics",
    "max_marks": 5,
    "criteria": [
        {"name": "definition", "marks": 1},
        {"name": "formula", "marks": 2},
        {"name": "explanation", "marks": 2}
    ]
}

math_rubric = {
    "subject": "math",
    "max_marks": 5,
    "criteria": [
        {"name": "steps", "marks": 2},
        {"name": "method", "marks": 2},
        {"name": "final_answer", "marks": 1}
    ]
}

english_rubric = {
    "subject": "english",
    "max_marks": 5,
    "criteria": [
        {"name": "key_points", "marks": 2},
        {"name": "clarity", "marks": 2},
        {"name": "language", "marks": 1}
    ]
}

fallback_rubric = {
    "subject": "generic",
    "max_marks": 5,
    "criteria": [
        {"name": "relevance", "marks": 1},
        {"name": "coverage", "marks": 1},
        {"name": "clarity", "marks": 1},
        {"name": "logic", "marks": 1},
        {"name": "language", "marks": 1}
    ]
}

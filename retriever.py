# retriever.py
from rubrics import physics_rubric, math_rubric, english_rubric, fallback_rubric

def get_rubric(question: str):
    q = question.lower()
    
    # Physics keywords
    if any(word in q for word in ["force", "mass", "acceleration", "newton", "gravity", "energy", "velocity", "physics"]):
        return physics_rubric
    
    # Math keywords
    elif any(word in q for word in ["solve", "equation", "integrate", "derivative", "calculus", "algebra", "geometry", "math"]):
        return math_rubric
    
    # English keywords
    elif any(word in q for word in ["explain", "essay", "poem", "story", "literature", "analysis", "summary", "theme"]):
        return english_rubric
    
    # Default fallback
    return fallback_rubric

# main.py
import sys
from retriever import get_rubric
from evaluator import evaluate_answer, evaluate_without_rubric
from utils import validate_input
import json

def main():
    print("\n" + "="*40)
    print("      Mini Answer Evaluator CLI")
    print("="*40 + "\n")
    
    question = input("Enter Question:\n> ")
    answer = input("\nEnter Student Answer:\n> ")
    
    is_valid, msg = validate_input(question, answer)
    if not is_valid:
        print(f"\n❌ Error: {msg}")
        return

    # Retrieve rubric
    rubric = get_rubric(question)
    print(f"\n[Retrieved Rubric: {rubric['subject'].capitalize()}]")
    
    print("\nEvaluating...", end="", flush=True)
    
    # Evaluate with rubric
    result = evaluate_answer(question, answer, rubric)
    print(" Done!")
    
    print("\n--- Evaluation Result ---")
    if "error" in result:
        print(f"Error: {result['error']}")
        if "raw_output" in result:
            print(f"Raw Output: {result['raw_output']}")
    else:
        print(f"Marks Awarded: {result.get('marks_awarded', 'N/A')} / {result.get('max_marks', 'N/A')}")
        print(f"Overall Feedback: {result.get('overall_feedback', 'No feedback provided')}")
        print(f"Justification: {result.get('justification', 'No justification provided')}")
        
        if "criteria_breakdown" in result:
            print("\nCriteria Breakdown:")
            for item in result["criteria_breakdown"]:
                print(f" - {item['criterion']}: {item['marks']}/{item['max_marks']}")
                print(f"   Feedback: {item['feedback']}")

    # Bonus: Compare
    compare = input("\nWould you like to see evaluation without rubric? (y/n): ")
    if compare.lower() == 'y':
        print("\nEvaluating without rubric...", end="", flush=True)
        result_no_rubric = evaluate_without_rubric(question, answer)
        print(" Done!")
        print("\n--- Comparison (No Rubric) ---")
        print(f"Marks Awarded: {result_no_rubric.get('marks_awarded', 'N/A')} / 5")
        print(f"Feedback: {result_no_rubric.get('feedback', 'No feedback')}")

    print("\n" + "="*40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

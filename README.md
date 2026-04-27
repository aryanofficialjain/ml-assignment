# Mini Answer Evaluator

A production-style system for evaluating student answers using rule-guided LLM logic.

## Approach<img width="1280" height="828" alt="Screenshot 2026-04-27 at 3 50 16 PM" src="https://github.com/user-attachments/assets/64063a23-a38e-4640-876c-e75718ac31e2" />


- **Keyword-based rubric retrieval**: Automatically maps questions to the correct evaluation criteria.
- **Structured rubric design**: Pre-defined marking schemes for Physics, Math, and English.
- **LLM-based evaluation**: Uses controlled prompts to ensure strict adherence to rubrics.

## Features

- **Rubric-based evaluation**: Precision grading using subject-specific rules.
- **JSON output**: Structured results including marks, feedback, and justification.
- **Streamlit UI**: Simple and effective interface for interaction.
- **Comparison mode**: Analyze the difference between rubric-guided and general evaluation.

## Prompt Strategy

- **Strict evaluation rules**: Prevents the model from making assumptions.
- **No assumptions**: Only awards marks for information explicitly present in the answer.
- **Structured JSON output**: Ensures consistent data format for integration.

## Improvements

- **Embeddings for better retrieval**: Use vector similarity instead of simple keyword matching.
- **Per-criteria scoring**: Implement a more granular breakdown of marks in the UI.
- **Fine-tuned evaluation model**: Train a model on specialized academic grading data.

---
ML Internship Project

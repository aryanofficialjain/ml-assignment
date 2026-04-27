# app.py
import streamlit as st
from retriever import get_rubric
from evaluator import evaluate_answer
from evaluator_no_rubric import evaluate_no_rubric

st.set_page_config(page_title="Mini Evaluator", layout="centered")

st.title("Mini Answer Evaluator")
st.write("Evaluate student answers using keyword-based rubric retrieval.")

# Input fields
question = st.text_area("Enter Question")
answer = st.text_area("Enter Student Answer")

# Mode selection
mode = st.radio(
    "Select Evaluation Mode",
    ["With Rubric", "Without Rubric"]
)

compare = st.checkbox("Compare both modes")

if st.button("Evaluate"):
    if not question or not answer:
        st.warning("Please fill all fields.")
    else:
        rubric = get_rubric(question)
        
        if compare:
            st.subheader("Comparison Analysis")
            with st.spinner("Processing both evaluations..."):
                result_with = evaluate_answer(question, answer, rubric)
                result_without = evaluate_no_rubric(question, answer)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("### With Rubric")
                st.write(f"**Detected Subject:** {rubric['subject'].capitalize()}")
                st.json(result_with)
            with col2:
                st.write("### Without Rubric")
                st.write("**Mode:** General Evaluation")
                st.json(result_without)
        else:
            if mode == "With Rubric":
                st.subheader("Retrieved Rubric")
                st.json(rubric)
                with st.spinner("Evaluating with rubric..."):
                    result = evaluate_answer(question, answer, rubric)
            else:
                with st.spinner("Evaluating without rubric..."):
                    result = evaluate_no_rubric(question, answer)
            
            st.subheader("Evaluation Result")
            st.json(result)

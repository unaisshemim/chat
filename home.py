import streamlit as st
import json

st.write("This is just a home page!")
questions = [
    "How long have you been in your current relationship?",
    "How satisfied are you with your relationship?",
    "How often do you and your partner communicate effectively?",
    "How often do you and your partner spend quality time together?",
    "How do you handle conflicts in your relationship?",
    "What are your relationship goals for the next year?",
    "How important is physical intimacy in your relationship?",
    "How do you and your partner support each other's personal growth?",
    "How do you and your partner manage finances together?",
    "How do you and your partner make important decisions together?",
    "Are you a day person or a night person?"
]

responses = {}

for i, question in enumerate(questions):
    if i == 0:
        responses[question] = st.radio(question, ["Less than a year", "1-3 years", "3-5 years", "More than 5 years"])
    elif i == 1:
        responses[question] = st.slider(question, 1, 10, 5)
    elif i == 2:
        responses[question] = st.radio(question, ["Never", "Rarely", "Sometimes", "Often", "Always"])
    elif i == 3:
        responses[question] = st.radio(question, ["Never", "Rarely", "Sometimes", "Often", "Always"])
    elif i == 4:
        responses[question] = st.radio(question, ["Avoid", "Argue", "Discuss calmly", "Seek help"])
    elif i == 5:
        responses[question] = st.text_input(question)
    elif i == 6:
        responses[question] = st.radio(question, ["Not important", "Somewhat important", "Very important", "Extremely important"])
    elif i == 7:
        responses[question] = st.radio(question, ["Not at all", "Somewhat", "Very much", "Extremely"])
    elif i == 8:
        responses[question] = st.radio(question, ["Not at all", "Somewhat", "Very well", "Extremely well"])
    elif i == 9:
        responses[question] = st.radio(question, ["Individually", "Together", "With advice from others", "Depends on the decision"])
    elif i == 10:
        responses[question] = st.radio(question, ["Day person", "Night person"])

if st.button("Save Responses"):
    if 'key' not in st.session_state:
        st.session_state['response'] = responses

    st.success("Responses saved successfully!")
import streamlit as st
from fuzzywuzzy import fuzz
from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.environ.get('HF_TOKEN'))

knowledge_base = {
    "What is credit risk?": "Credit risk is when someone might not pay back a loan, so the bank could lose money. It’s like lending your toy and not getting it back. Banks use math to guess if someone is risky.",
    "What is data democratization?": "Data democratization means everyone can use data to make choices; it's like turning a complicated chemistry lab into a fun, safe kitchen where everyone can cook. It helps people understand numbers without being experts.",
    "What is an algorithm?": "An algorithm is like a recipe or step-by-step instructions for solving a problem! Just like following steps to bake cookies, computers follow algorithms to complete tasks."
}

relevant_keywords = [
    "data", "science", "analytics", "risk", "credit", "model", "modeling",
    "geospatial", "democratization", "predictive", "machine learning", "statistics",
    "lake", "llm", "large language model", "fraud", "forecasting", "financial",
    "neural", "network", "algorithm"
]

def is_on_topic(user_input):
    user_input_lower = user_input.lower()
    return any(keyword in user_input_lower for keyword in relevant_keywords)

def find_closest_question(user_input):
    best_match = None
    highest_score = 0
    for question in knowledge_base:
        score = fuzz.partial_ratio(user_input.lower(), question.lower())
        if score > highest_score and score > 85:
            highest_score = score
            best_match = question
    return best_match

def get_llm_answer(user_input):
    prompt = f"Explain {user_input} in 100 words or less, like you're talking to a 10-year-old, in the context of data science or analytics. Keep it simple and clear."
    try:
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            max_tokens=150,  # ~100 words
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I couldn't get an answer right now: {str(e)}"

st.title("DataBite Chatbot")
st.write("Ask about data science or analytics in simple terms!")

user_input = st.text_input("Your question:", "")
if user_input:
    if not is_on_topic(user_input):
        st.write("**Answer**: This is out of my domain.")
    else:
        closest_question = find_closest_question(user_input)
        if closest_question:
            st.write("**Answer**: ", knowledge_base[closest_question])
        else:
            st.write("**Answer**: ", get_llm_answer(user_input))

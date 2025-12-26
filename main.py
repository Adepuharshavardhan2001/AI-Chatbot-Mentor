import os
import asyncio
from dotenv import load_dotenv

# -----------------------------------------
# FIX STREAMLIT + GEMINI EVENT LOOP ISSUE
# -----------------------------------------
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# -----------------------------------------
# LOAD ENV VARIABLES
# -----------------------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing. Check your .env file")

import streamlit as st
from datetime import datetime

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: #e5e7eb;
}
h1 {
    background: linear-gradient(90deg, #38bdf8, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1.2rem;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #6366f1, #a855f7);
}
.stDownloadButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
}
.stDownloadButton>button:hover {
    background-color: #16a34a;
}
</style>
""", unsafe_allow_html=True)

MODULES = [
    "Python",
    "SQL",
    "Power BI",
    "Exploratory Data Analysis (EDA)",
    "Machine Learning (ML)",
    "Deep Learning (DL)",
    "Generative AI (Gen AI)",
    "Agentic AI",
]

if "module" not in st.session_state:
    st.session_state.module = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def build_prompt(selected_module: str):
    system_prompt = f"""
You are an AI Mentor specialized ONLY in {selected_module}.
Rules:
- Answer ONLY questions related to {selected_module}
- If the question is NOT related to {selected_module}, respond EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."
- Be clear, structured, and educational
"""
    return ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template("{question}")
    ])

st.title(" AI Chatbot Mentor")
st.write("Your domain-focused AI learning assistant")

if st.session_state.module is None:
    st.subheader(" Select a Learning Module")
    selected = st.selectbox(
        "Choose your domain",
        ["-- Select --"] + MODULES
    )
    if selected != "-- Select --":
        st.session_state.module = selected
        st.rerun()
else:
    st.subheader(f" {st.session_state.module} Mentor")
    st.info(
        f"Welcome to **{st.session_state.module} AI Mentor** \n"
        "Ask anything related to this module."
    )

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").markdown(f" **You:** {msg}")
        else:
            st.chat_message("assistant").markdown(f" **Mentor:** {msg}")

    user_input = st.chat_input("Type your question here...")

    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        prompt = build_prompt(st.session_state.module)
        response = llm.invoke(
            prompt.format_messages(question=user_input)
        )
        st.session_state.chat_history.append(("assistant", response.content))
        st.rerun()

    if st.session_state.chat_history:
        st.divider()
        st.subheader(" Download Session Notes")
        chat_text = ""
        for role, msg in st.session_state.chat_history:
            prefix = "You" if role == "user" else "AI Mentor"
            chat_text += f"{prefix}: {msg}\n\n"
        file_name = f"AI_Mentor_{st.session_state.module}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        st.download_button(
            label=" Download Conversation",
            data=chat_text,
            file_name=file_name,
            mime="text/plain"
        )

    st.divider()
    if st.button(" Change Module / Restart"):
        st.session_state.module = None
        st.session_state.chat_history = []
        st.rerun()

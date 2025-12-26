# AI Chatbot Mentor

An interactive, module-specific AI mentoring application designed to provide focused and structured learning guidance instead of generic chatbot responses.

---

## Project Overview

AI Chatbot Mentor addresses a common challenge faced by learners:  
general-purpose AI chatbots often provide mixed or unfocused answers across multiple domains, which can confuse beginners.

This application introduces **domain-restricted AI mentoring**, where the chatbot responds strictly within a selected learning module. If a question is asked outside the chosen domain, the AI politely refuses to answer, ensuring clarity, relevance, and structured learning.

---

## Key Features

- Module-specific AI mentoring system
- Strict domain control using system prompts
- Supported learning modules:
  - Python
  - SQL
  - Power BI
  - Exploratory Data Analysis (EDA)
  - Machine Learning (ML)
  - Deep Learning (DL)
  - Generative AI (Gen AI)
  - Agentic AI
- Interactive chat-based interface
- Session-based chat history
- Downloadable conversation notes
- Clean and responsive Streamlit UI

---

## Tech Stack

- Python
- Streamlit
- Google Gemini LLM
- LangChain (Prompt Templates)
- Python-dotenv
- AsyncIO (event loop handling)

---

## How It Works

1. User selects a learning module
2. The AI mentor is restricted to the selected domain only
3. User asks questions related to the chosen module
4. AI responds with clear, structured explanations
5. If a question is outside the selected domain, the AI politely refuses to answer
6. Chat history is maintained during the session
7. Conversation notes can be downloaded as a text file

---

## Environment Setup

Create a `.env` file in the project root directory and add:

GOOGLE_API_KEY=your_api_key_here


> Note: The `.env` file is ignored using `.gitignore` to keep API keys secure.

---

## How to Run the Application

1. Install dependencies:
pip install -r requirements.txt


2. Run the Streamlit app:
streamlit run main.py


3. Select a learning module and start asking questions

---

## Use Cases

- Beginners learning technical subjects
- Focused self-study sessions
- Domain-restricted AI mentoring
- Structured learning without distractions

---

## Acknowledgement

Thanks to my mentors for their guidance and continuous support in designing this project and helping me understand structured prompt design, domain control, and application-level AI development.



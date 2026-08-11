import streamlit as st
from google import genai
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main page */
.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #4b5563;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: #ffffff;
    padding: 0;
    border-radius: 18px;
    border: 1px solid #d1d5db;
    margin-bottom: 20px;
    overflow: hidden;
}

.card-title {
    background: #111827;
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    padding: 15px 20px;
    margin: 0;
}

.card-content {
    color: #374151;
    font-size: 16px;
    padding: 18px 20px;
    background: #ffffff;
}

/* Answer box */
.answer-box {
    background: #ffffff;
    padding: 0;
    border-radius: 18px;
    border: 1px solid #d1d5db;
    margin-top: 20px;
    overflow: hidden;
}

.answer-title {
    background: #111827;
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
    padding: 16px 20px;
}

/* Input section */
.input-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #d1d5db;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ---------------- GEMINI API ----------------

api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(
    api_key=api_key
)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 🎓 StudyMate AI")

    st.write("Your personal AI learning assistant.")

    st.divider()

    st.markdown("### 📚 Study Options")

    mode = st.selectbox(
        "Learning Mode",
        [
            "Concept Explanation",
            "Quick Answer",
            "Detailed Explanation",
            "Example Based Learning"
        ]
    )

    st.divider()

    st.markdown("### 💡 Study Tip")

    st.info(
        "Ask clear questions and mention "
        "the topic you are studying."
    )


# ---------------- MAIN HEADER ----------------

st.markdown(
    '<div class="main-title">🎓 StudyMate AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn smarter with your personal AI study assistant.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- TOP CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">📖 Learn</div>
        <div class="card-content">
            Understand difficult concepts easily with simple explanations.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">💬 Ask</div>
        <div class="card-content">
            Ask questions and get clear answers from your AI assistant.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">🚀 Improve</div>
        <div class="card-content">
            Learn with examples and improve your understanding.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------

st.markdown("""
<div class="input-box">
    <h3>📚 What are you studying?</h3>
</div>
""", unsafe_allow_html=True)


topic = st.text_input(
    "Study Topic",
    placeholder="Example: Python, Machine Learning, Java..."
)


question = st.text_area(
    "Your Question",
    placeholder="Example: What is supervised learning?",
    height=130
)


# ---------------- ASK BUTTON ----------------

if st.button(
    "🚀 Ask StudyMate",
    use_container_width=True
):

    if not topic:

        st.warning(
            "⚠️ Please enter a study topic."
        )

    elif not question:

        st.warning(
            "⚠️ Please enter your question."
        )

    else:

        prompt = f"""
You are StudyMate AI, an intelligent educational assistant.

Study Topic:
{topic}

Learning Mode:
{mode}

Student Question:
{question}

Instructions:

- Explain the concept clearly.
- Use simple language.
- Give examples when useful.
- Organize the answer using headings.
- Use bullet points where appropriate.
- Explain step by step when necessary.
- Help the student understand the concept.
- Avoid unnecessarily complicated terminology.
"""

        with st.spinner(
            "🧠 StudyMate is preparing your answer..."
        ):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )


        # ---------------- ANSWER ----------------

        st.markdown("""
        <div class="answer-box">
            <div class="answer-title">
                🤖 StudyMate Answer
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.write(response.text)

import streamlit as st
from google import genai
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* ================= MAIN PAGE ================= */

.main {
    background-color: #0b1120;
}

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* ================= MAIN TITLE ================= */

.main-title {
    color: #ffffff !important;
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}

.subtitle {
    color: #d1d5db !important;
    font-size: 18px;
    margin-bottom: 30px;
}

/* ================= TOP CARDS ================= */

.card {
    background: #ffffff;
    border-radius: 18px;
    border: 1px solid #374151;
    margin-bottom: 20px;
    overflow: hidden;
}

.card-title {
    background: #172033;
    color: #ffffff !important;
    font-size: 22px;
    font-weight: 800;
    padding: 17px 20px;
}

.card-content {
    background: #ffffff;
    color: #1f2937 !important;
    font-size: 16px;
    line-height: 1.5;
    padding: 18px 20px;
}

/* ================= STUDY SECTION ================= */

.study-header {
    background: #172033;
    color: #ffffff !important;
    font-size: 24px;
    font-weight: 800;
    padding: 18px 22px;
    border-radius: 18px 18px 0 0;
    border: 1px solid #374151;
}

.study-container {
    background: #ffffff;
    padding: 22px;
    border-radius: 0 0 18px 18px;
    border: 1px solid #374151;
    border-top: none;
    margin-bottom: 25px;
}

/* ================= STREAMLIT LABELS ================= */

label {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Input text */

input {
    color: #ffffff !important;
}

/* Text area */

textarea {
    color: #ffffff !important;
}

/* Placeholder */

input::placeholder,
textarea::placeholder {
    color: #9ca3af !important;
}

/* ================= ANSWER ================= */

.answer-header {
    background: #172033;
    color: #ffffff !important;
    font-size: 24px;
    font-weight: 800;
    padding: 18px 22px;
    border-radius: 18px 18px 0 0;
    margin-top: 25px;
    border: 1px solid #374151;
}

.answer-content {
    background: #ffffff;
    color: #1f2937 !important;
    padding: 25px;
    border-radius: 0 0 18px 18px;
    border: 1px solid #374151;
    border-top: none;
    font-size: 16px;
    line-height: 1.6;
}

/* ================= SIDEBAR ================= */

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* ================= BUTTON ================= */

.stButton > button {
    background-color: #172033;
    color: #ffffff !important;
    border: 1px solid #4b5563;
    border-radius: 12px;
    font-weight: 700;
    padding: 12px;
}

.stButton > button:hover {
    background-color: #26344d;
    color: #ffffff !important;
}

/* ================= DIVIDER ================= */

hr {
    border-color: #374151 !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# GEMINI API
# =====================================================

api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(
    api_key=api_key
)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown(
        "## 🎓 StudyMate AI"
    )

    st.write(
        "Your personal AI learning assistant."
    )

    st.divider()

    st.markdown(
        "### 📚 Study Options"
    )

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

    st.markdown(
        "### 💡 Study Tip"
    )

    st.info(
        "Ask clear questions and mention "
        "the topic you are studying."
    )


# =====================================================
# MAIN TITLE
# =====================================================

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


# =====================================================
# TOP CARDS
# =====================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            📖 Learn
        </div>

        <div class="card-content">
            Understand difficult concepts easily
            with simple explanations.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            💬 Ask
        </div>

        <div class="card-content">
            Ask questions and get clear answers
            from your AI assistant.
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            🚀 Improve
        </div>

        <div class="card-content">
            Learn with examples and improve
            your understanding.
        </div>

    </div>
    """, unsafe_allow_html=True)


# =====================================================
# STUDY INPUT SECTION
# =====================================================

st.markdown("""
<div class="study-header">
    📚 What are you studying?
</div>

<div class="study-container">
</div>
""", unsafe_allow_html=True)


# =====================================================
# TOPIC INPUT
# =====================================================

topic = st.text_input(
    "Study Topic",
    placeholder="Example: Python, Machine Learning, Java..."
)


# =====================================================
# QUESTION INPUT
# =====================================================

question = st.text_area(
    "Your Question",
    placeholder="Example: What is supervised learning?",
    height=140
)


# =====================================================
# ASK BUTTON
# =====================================================

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

        # =============================================
        # PROMPT
        # =============================================

        prompt = f"""
You are StudyMate AI, an intelligent educational assistant.

Study Topic:
{topic}

Learning Mode:
{mode}

Student Question:
{question}

Instructions:

1. Explain the concept clearly.
2. Use simple language.
3. Give examples when useful.
4. Use headings and bullet points.
5. Explain step by step when necessary.
6. Help the student understand the concept.
7. Avoid unnecessarily complicated terminology.
"""

        # =============================================
        # GENERATE ANSWER
        # =============================================

        with st.spinner(
            "🧠 StudyMate is preparing your answer..."
        ):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )


        # =============================================
        # DISPLAY ANSWER
        # =============================================

        st.markdown("""
        <div class="answer-header">
            🤖 StudyMate Answer
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="answer-content">',
            unsafe_allow_html=True
        )

        st.write(response.text)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

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
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

.card-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Answer box */
.answer-box {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #ddd;
    margin-top: 20px;
}

.answer-title {
    font-size: 22px;
    font-weight: 600;
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


# ---------------- API ----------------

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

    st.markdown("### 💡 Tip")

    st.info(
        "Ask clear questions and mention "
        "the topic you are studying."
    )


# ---------------- MAIN PAGE ----------------

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
        Understand difficult concepts easily.
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">💬 Ask</div>
        Ask questions and get instant answers.
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">🚀 Improve</div>
        Learn with examples and explanations.
    </div>
    """, unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">📚 What are you studying?</div>',
    unsafe_allow_html=True
)

topic = st.text_input(
    "Topic",
    placeholder="Example: Python, Machine Learning, Java..."
)

question = st.text_area(
    "Your Question",
    placeholder="Example: What is supervised learning?",
    height=130
)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------- ASK BUTTON ----------------

if st.button(
    "🚀 Ask StudyMate",
    use_container_width=True
):

    if not topic:

        st.warning("⚠️ Please enter a study topic.")

    elif not question:

        st.warning("⚠️ Please enter your question.")

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
- Explain clearly.
- Use simple language.
- Give examples when useful.
- Organize the answer using headings or bullet points.
- Help the student understand the concept rather than just giving
  a short answer.
"""

        with st.spinner("🧠 StudyMate is preparing your answer..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        # ---------------- ANSWER ----------------

        st.markdown(
            '<div class="answer-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="answer-title">🤖 StudyMate Answer</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.write(response.text)

        st.markdown("</div>", unsafe_allow_html=True)

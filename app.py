import streamlit as st
from google import genai
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# GEMINI API
# --------------------------------------------------

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

client = genai.Client(api_key=api_key)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 20px;
    margin-bottom: 30px;
}

.card-container {
    display: flex;
    gap: 20px;
    margin-top: 20px;
    margin-bottom: 30px;
}

.study-card {
    flex: 1;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #444;
    background-color: #1f2430;
    min-height: 150px;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 15px;
}

.card-content {
    font-size: 17px;
    line-height: 1.6;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    padding: 20px;
    border-radius: 15px;
    background-color: #182238;
    margin-top: 20px;
    margin-bottom: 20px;
}

.answer-box {
    padding: 25px;
    border-radius: 15px;
    background-color: #1e2533;
    border: 1px solid #444;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🎓 StudyMate AI")

    st.write("Your personal AI learning assistant.")

    st.divider()

    st.markdown("### 📚 Study Options")

    learning_mode = st.selectbox(
        "Learning Mode",
        [
            "Concept Explanation",
            "Question & Answer",
            "Improve Understanding"
        ]
    )

    st.divider()

    st.markdown("### 💡 Study Tip")

    st.info(
        "Ask clear questions and mention the topic you are studying."
    )

# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------

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

# --------------------------------------------------
# THREE CARDS
# --------------------------------------------------

st.markdown("""
<div class="card-container">

    <div class="study-card">
        <div class="card-title">📖 Learn</div>
        <div class="card-content">
            Understand difficult concepts easily with simple explanations.
        </div>
    </div>

    <div class="study-card">
        <div class="card-title">💬 Ask</div>
        <div class="card-content">
            Ask questions and get clear answers from your AI assistant.
        </div>
    </div>

    <div class="study-card">
        <div class="card-title">🚀 Improve</div>
        <div class="card-content">
            Learn with examples and improve your understanding.
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# STUDY SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📚 What are you studying?</div>',
    unsafe_allow_html=True
)

topic = st.text_input(
    "Study Topic",
    placeholder="Example: Python, Machine Learning, Java..."
)

question = st.text_area(
    "Your Question",
    placeholder="Example: What is supervised learning?"
)

# --------------------------------------------------
# BUTTON
# --------------------------------------------------

if st.button("🤖 Get Answer", use_container_width=True):

    if not topic:
        st.warning("Please enter a study topic.")

    elif not question:
        st.warning("Please enter your question.")

    else:

        # ------------------------------------------
        # PROMPT
        # ------------------------------------------

        if learning_mode == "Concept Explanation":

            prompt = f"""
You are StudyMate AI, a friendly educational assistant.

The student is studying:
{topic}

The student's question is:
{question}

Explain the concept in a simple and easy-to-understand way.

Follow this structure:

1. Simple Definition
2. Detailed Explanation
3. Basic Example
4. Real-world Application
5. Key Points

Use simple language suitable for a student.
"""

        elif learning_mode == "Question & Answer":

            prompt = f"""
You are StudyMate AI.

The student is studying:
{topic}

Student's question:
{question}

Give a clear and accurate answer.

Use this structure:

1. Direct Answer
2. Explanation
3. Example
4. Important Points

Keep the explanation easy to understand.
"""

        else:

            prompt = f"""
You are StudyMate AI.

The student is studying:
{topic}

Student's question:
{question}

Help the student improve their understanding.

Follow this structure:

1. Explain the concept simply
2. Give an example
3. Explain a common mistake
4. Give a real-world application
5. Give a short practice question

Use simple student-friendly language.
"""

        # ------------------------------------------
        # GENERATE ANSWER
        # ------------------------------------------

        with st.spinner("🤖 StudyMate AI is thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                st.markdown(
                    '<div class="answer-box">',
                    unsafe_allow_html=True
                )

                st.subheader("🤖 StudyMate AI")

                st.markdown(response.text)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    "Unable to generate the answer. "
                    "Please check your Gemini API key and try again."
                )

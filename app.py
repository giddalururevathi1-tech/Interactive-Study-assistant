import streamlit as st
from google import genai

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Interactive Study Assistant",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("📚 Interactive Study Assistant")
st.write("Learn smarter with your personal AI study assistant.")

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("🎓 StudyMate AI")
    st.write("Your personal AI learning assistant.")

    st.divider()

    st.subheader("📚 Study Options")

    mode = st.selectbox(
        "Learning Mode",
        [
            "Concept Explanation",
            "Simple Explanation",
            "Detailed Explanation",
            "Example",
            "Exam Preparation"
        ]
    )

    st.divider()

    st.subheader("💡 Study Tip")

    st.info(
        "Ask clear questions and mention "
        "the topic you are studying."
    )

# -----------------------------
# Introduction Cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("📖 Learn")

        st.write(
            "Understand difficult concepts "
            "with simple explanations."
        )

with col2:

    with st.container(border=True):

        st.subheader("💬 Ask")

        st.write(
            "Ask questions and get clear answers "
            "from your AI study assistant."
        )

with col3:

    with st.container(border=True):

        st.subheader("🚀 Improve")

        st.write(
            "Learn with examples and improve "
            "your understanding."
        )

# -----------------------------
# Study Topic
# -----------------------------

st.header("📚 What are you studying?")

topic = st.text_input(
    "Study Topic",
    placeholder="Example: Python, Machine Learning, Java..."
)

# -----------------------------
# Question
# -----------------------------

question = st.text_area(
    "Your Question",
    placeholder="Example: What is supervised learning?",
    height=120
)

# -----------------------------
# Get Answer Button
# -----------------------------

if st.button("🤖 Get Answer", use_container_width=True):

    if not topic:

        st.warning("⚠️ Please enter a study topic.")

    elif not question:

        st.warning("⚠️ Please enter your question.")

    else:

        # -----------------------------
        # Gemini API
        # -----------------------------

        try:

            api_key = st.secrets["GEMINI_API_KEY"]

            client = genai.Client(
                api_key=api_key
            )

            # -----------------------------
            # Prompt
            # -----------------------------

            prompt = f"""
You are an Interactive Study Assistant.

The student is studying:
{topic}

Learning mode:
{mode}

Student's question:
{question}

Give a clear and educational answer.

Follow these instructions:

1. Explain the concept in simple language.
2. Use headings where useful.
3. Give a basic example.
4. If appropriate, give a real-world example.
5. Keep the answer suitable for a student.
6. Do not make the answer unnecessarily complicated.
7. If the topic involves programming, provide a simple code example.
"""

            # -----------------------------
            # Generate Answer
            # -----------------------------

            with st.spinner("🤖 Generating answer..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

            # -----------------------------
            # Display Answer
            # -----------------------------

            st.success("Answer generated successfully!")

            st.subheader("🤖 AI Study Assistant")

            st.markdown(response.text)

        except KeyError:

            st.error(
                "❌ GEMINI_API_KEY is not configured. "
                "Please add it in Streamlit Secrets."
            )

        except Exception as e:

            st.error(
                "❌ Something went wrong while "
                "generating the answer."
            )

            st.write("Please check your Gemini API key and try again.")

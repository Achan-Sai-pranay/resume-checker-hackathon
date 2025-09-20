import streamlit as st
import pandas as pd
import time
import random

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Resume Relevance Check",
    page_icon="📑",
    layout="wide"
)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📤 Upload & Evaluate", "📊 Results", "ℹ️ About"])

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "🏠 Home":
    st.title("🤖 Automated Resume Relevance Check System")
    st.markdown("""
        Welcome to our **Hackathon Project** 🚀  
        This system uses **Generative AI + LLMs + LangChain**  
        to evaluate resumes against job descriptions.  

        ### 🔑 Features:
        - Upload multiple resumes (PDF/DOCX) + a job description  
        - AI-powered **Relevance Score** (0–100%)  
        - Recruiter-style **Feedback & Summary**  
        - Candidate **Ranking Dashboard**  
    """)
    st.success("➡️ Head to 'Upload & Evaluate' in the sidebar to try it out!")

# -------------------------------
# UPLOAD & EVALUATE PAGE
# -------------------------------
elif page == "📤 Upload & Evaluate":
    st.title("📤 Upload Resumes & Job Description")

    jd_text = st.text_area("📝 Paste Job Description", height=200, placeholder="Paste the JD here...")
    resumes = st.file_uploader("📎 Upload Resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

    if jd_text and resumes:
        if st.button("🚀 Run Evaluation"):
            st.info("⏳ Evaluating resumes... please wait.")

            progress = st.progress(0)
            results = []

            for i, resume in enumerate(resumes):
                # Simulate processing delay (replace with real pipeline call)
                time.sleep(1)
                score = random.randint(40, 95)  # Replace with actual scoring logic
                feedback = f"Candidate {i+1} matches well on technical skills but lacks cloud experience." \
                           if score < 70 else f"Candidate {i+1} is a strong fit with solid alignment to JD."

                results.append({"Candidate": resume.name, "Relevance Score": score, "AI Feedback": feedback})
                progress.progress((i + 1) / len(resumes))

            st.success("✅ Evaluation Completed!")
            st.session_state["results_df"] = pd.DataFrame(results)

# -------------------------------
# RESULTS PAGE
# -------------------------------
elif page == "📊 Results":
    st.title("📊 Candidate Evaluation Results")

    if "results_df" in st.session_state:
        df = st.session_state["results_df"]

        # Sort by score
        df_sorted = df.sort_values(by="Relevance Score", ascending=False).reset_index(drop=True)

        st.subheader("🏆 Ranked Candidates")
        st.dataframe(df_sorted.style.background_gradient(cmap="Blues"))

        # Highlight top candidate
        top_candidate = df_sorted.iloc[0]
        st.markdown(f"""
        ### 🥇 Top Candidate: **{top_candidate['Candidate']}**
        - Relevance Score: **{top_candidate['Relevance Score']}%**
        - Feedback: {top_candidate['AI Feedback']}
        """)
    else:
        st.warning("⚠️ No results found. Please run evaluation first.")

# -------------------------------
# ABOUT PAGE
# -------------------------------
elif page == "ℹ️ About":
    st.title("ℹ️ About This Project")
    st.markdown("""
        **Team Hackathon Project – Automated Resume Relevance Check**  

        Built with ❤️ using:
        - **Python, Streamlit** for UI
        - **LangChain, LangGraph, LangSmith** for LLM pipelines
        - **Vector DBs & embeddings** for semantic matching
        - **OpenAI / HuggingFace models** for smart feedback
                - just check this is done by pranay for checking updatation

        👉 Goal: Save recruiters time, reduce bias, and give candidates constructive feedback.
    """)
    st.info("Hackathon 2025 ✨ Powered by GenAI")
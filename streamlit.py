import streamlit as st
import requests
import pandas as pd

# Inject custom CSS to style the page
def inject_css():
    st.markdown("""
    <style>
    /* Global background */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #fffaf0, #fef6e4);
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
    }

    /* Top navbar */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: #fffaf0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        padding: 14px 28px;
        z-index: 999;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar h1 {
        font-size: 22px;
        color: #333;
        margin: 0;
        font-weight: 600;
    }
    .navbar a {
        margin-left: 24px;
        text-decoration: none;
        color: #ff9800;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .navbar a:hover {
        color: #e65100;
        text-shadow: 0 0 8px #ffc107;
    }

    /* Sidebar styles */
    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 250px;
        height: 100vh;
        background-color: #fffaf0;
        box-shadow: 2px 0 8px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        transform: translateX(-100%);
    }
    .sidebar.open {
        transform: translateX(0);
    }
    .sidebar .menu {
        display: flex;
        flex-direction: column;
        padding: 20px;
    }
    .sidebar a {
        margin-bottom: 16px;
        text-decoration: none;
        color: #ff9800;
        font-weight: 600;
    }
    .sidebar a:hover {
        color: #e65100;
    }

    /* Hamburger menu */
    .hamburger {
        cursor: pointer;
        display: block;
        width: 30px;
        height: 3px;
        background-color: #333;
        border-radius: 5px;
        margin-top: 7px;
        transition: all 0.3s ease;
    }
    .hamburger.open {
        background-color: transparent;
    }
    .hamburger.open::before {
        content: "";
        position: absolute;
        top: 0;
        width: 30px;
        height: 3px;
        background-color: #333;
        transform: rotate(45deg);
        transition: all 0.3s ease;
    }
    .hamburger.open::after {
        content: "";
        position: absolute;
        bottom: 0;
        width: 30px;
        height: 3px;
        background-color: #333;
        transform: rotate(-45deg);
        transition: all 0.3s ease;
    }

    /* Central content styling */
    .content {
        margin-left: 50px; /* Adjust the content width */
        padding-top: 100px;
    }

    /* Card styling */
    .neoncard {
        background: #fcf8f3;
        border-radius: 28px;
        padding: 36px;
        margin-top: 100px;
        box-shadow: 0 10px 30px rgba(255, 224, 189, 0.4);
        animation: slideUp 1s ease-out;
    }

    /* Animations */
    @keyframes slideUp {
        from {opacity: 0; transform: translateY(40px);}
        to {opacity: 1; transform: translateY(0);}
    }

    /* Progress bar */
    .progbar-wrap {
        background: #f7f3eb;
        border-radius: 14px;
        padding: 6px;
        margin-top: 18px;
        margin-bottom: 12px;
        box-shadow: inset 0 0 8px 3px #ffefcd;
    }
    .progbar-fill {
        height: 28px;
        border-radius: 14px;
        background: linear-gradient(90deg, #ffce70, #ffc042);
        animation: fillBar 2s forwards;
        box-shadow: 0 0 20px #ffb300aa, 0 0 30px #ffbf0088;
        width: var(--fill-width);
    }
    @keyframes fillBar {
        from {width: 0;}
        to {width: var(--fill-width);}
    }

    /* Verdict tags */
    .verdict-High {
        background: #b9ecb7;
        color: #256920;
        border-radius: 24px;
        padding: 8px 24px;
        font-weight: 700;
    }
    .verdict-Medium {
        background: #fff1b3;
        color: #7f6d00;
        border-radius: 24px;
        padding: 8px 26px;
        font-weight: 700;
    }
    .verdict-Low {
        background: #f8b5b5;
        color: #6a1c1c;
        border-radius: 24px;
        padding: 8px 26px;
        font-weight: 700;
    }

    /* Table container */
    .table-container {
        max-height: 420px;
        overflow-y: auto;
        border-radius: 26px;
        box-shadow: 0 0 44px 18px #fcebbe77 inset;
        background-color: #fff9f0;
        padding: 18px;
        border: 1px solid #fee6b0;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # JavaScript for toggling the sidebar
    st.markdown("""
    <script>
    function toggleSidebar() {
        var sidebar = document.querySelector(".sidebar");
        var hamburger = document.querySelector(".hamburger");
        sidebar.classList.toggle("open");
        hamburger.classList.toggle("open");
    }
    </script>
    """, unsafe_allow_html=True)

inject_css()

# Sidebar with links for different pages
def sidebar():
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.markdown("""
    <div class="menu">
        <a href="#upload">📄 Upload Resume</a>
        <a href="#results">📊 Results Dashboard</a>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Upload Resume Page
def upload_resume_page():
    API_URL = "http://127.0.0.1:8000"
    st.markdown('<div class="neoncard" id="upload">', unsafe_allow_html=True)
    st.header("📄 Upload Resume & Evaluate")

    resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    job_id = st.text_input("Enter Job Description ID (optional)")

    if st.button("Evaluate 🚀"):
        if resume_file:
            with st.spinner("Evaluating resume..."):
                files = {"resume_file": resume_file.getbuffer()}
                resp = requests.post(f"{API_URL}/upload_resume", files=files)
                if resp.status_code == 200:
                    eval_resp = requests.post(
                        f"{API_URL}/evaluate",
                        json={"job_id": job_id, "resume_name": resume_file.name},
                    )
                    if eval_resp.status_code == 200:
                        result = eval_resp.json()
                        relevance = max(0, min(int(result.get("relevance_score", 0)), 100))
                        missing = result.get("missing", [])
                        verdict = result.get("verdict", "Medium")
                        feedback = result.get("feedback", "")

                        st.markdown(f"""
                        <div class="progbar-wrap">
                            <div class="progbar-fill" style="--fill-width:{relevance}%;"></div>
                        </div>
                        <h3 style="text-align:center;">Relevance Score: <b>{relevance}%</b></h3>
                        <p><b>Missing Skills:</b> <span style="color:#bf360c;">{', '.join(missing)}</span></p>
                        <p><b>Verdict:</b> <span class="verdict-{verdict}">{verdict}</span></p>
                        <p><b>Feedback:</b><br>{feedback}</p>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Evaluation failed.")
                else:
                    st.error("Upload failed.")
        else:
            st.warning("Please upload a resume file.")
    st.markdown("</div>", unsafe_allow_html=True)

# Results Dashboard Page
def results_dashboard_page():
    API_URL = "http://127.0.0.1:8000"
    st.markdown('<div class="neoncard" id="results">', unsafe_allow_html=True)
    st.header("📊 Results Dashboard")

    resp = requests.get(f"{API_URL}/results")
    if resp.status_code != 200:
        st.error("Failed to load results.")
        return

    results = resp.json()
    if not results:
        st.info("No evaluation results available.")
        return

    df = pd.DataFrame(results)
    min_score = st.slider("Minimum Relevance Score", 0, 100, 50)
    selected_verdicts = st.multiselect("Select Verdicts", df["verdict"].unique(), default=list(df["verdict"].unique()))
    filtered = df[(df["relevance_score"] >= min_score) & (df["verdict"].isin(selected_verdicts))]

    def verdict_tag(v): return f'<span class="verdict-{v}">{v}</span>'
    filtered["verdict_tag"] = filtered["verdict"].apply(verdict_tag)

    if not filtered.empty:
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        st.markdown(filtered.to_html(
            escape=False,
            index=False,
            columns=["resume_name", "job_id", "relevance_score", "verdict_tag", "missing", "feedback"]
        ), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No results match current filters.")
    st.markdown("</div>", unsafe_allow_html=True)

# Main routing based on sidebar clicks
if st.button("Open Sidebar"):
    sidebar()

if st.sidebar.radio("Go to", ["📄 Upload Resume", "📊 Results Dashboard"]) == "📄 Upload Resume":
    upload_resume_page()
else:
    results_dashboard_page()
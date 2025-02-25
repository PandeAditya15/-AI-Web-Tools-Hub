import streamlit as st

# Custom CSS with Teal Gradient Accents
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #1e1e2e, #121212); 
        color: white;
        margin: 0;
        padding: 0;
    }

    .big-title { 
        font-size: 30px !important; 
        font-weight: bold; 
        text-align: center; 
        background: linear-gradient(to right, #1abc9c, #3498db);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .sub-title { 
        font-size: 22px !important; 
        font-weight: bold; 
        text-align: center; 
        color: #bbbbbb; 
        margin-top: 5px;
    }

    .description { 
        font-size: 18px !important; 
        text-align: center; 
        color: #cccccc; 
        margin-bottom: 10px; 
    }

    .feature-box {
        background: linear-gradient(135deg, #2c3e50, #1abc9c); / Teal Gradient /
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 3px 3px 12px rgba(0, 255, 255, 0.2);
        border: 2px solid rgba(26, 188, 156, 0.3);
    }

    .feature-title {
        font-size: 20px !important; 
        font-weight: bold; 
        color: #1abc9c;
        margin-bottom: 10px;
    }

    .footer { 
        font-size: 14px !important; 
        text-align: center; 
        color: #bbbbbb; 
        margin-top: 50px; 
    }

    .button-container { 
        display: flex; 
        justify-content: center; 
        gap: 20px; 
        margin-top: 20px; 
    }

    .rounded-corner { 
        background: linear-gradient(to top right, #1abc9c, #16a085); 
        border-radius: 15px; 
        padding: 10px; 
        color: white; 
        font-size: 18px;
        margin-bottom: 20px; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.markdown("## 🔹 Select a Tool")

if st.sidebar.button("📹 Tutor.AI - YouTube Summarizer", key="sidebar_yt"):
    st.query_params["page"] = "app_UI"
    st.rerun()

if st.sidebar.button("📄 ATS Resume Scanner & Job Finder", key="sidebar_ats"):
    st.query_params["page"] = "app_ATS"
    st.rerun()

# Main Title with Gradient Text
st.markdown('<p class="big-title">🌟 AI Web Tools Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Boost Productivity with AI</p>', unsafe_allow_html=True)

# Project Description with Rounded Corner Teal Accent
st.markdown(
    '<div class="rounded-corner">'
    "🚀 This platform provides AI-powered solutions to help you learn, summarize, and apply smarter. "
    "Choose a tool below to get started!"
    "</div>",
    unsafe_allow_html=True
)

# Features Section
st.markdown('<div class="feature-box">', unsafe_allow_html=True)

st.markdown('<p class="feature-title">📹 Tutor.AI - YouTube Summarizer</p>', unsafe_allow_html=True)
st.markdown(
    """
    🔹 Instantly summarize long YouTube videos into concise insights.  
    🔹 Extract key points, timestamps, and topic highlights.  
    🔹 Supports AI-driven text summarization to make learning fast & efficient.  
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="feature-title">📄 ATS Resume Scanner & Job Finder</p>', unsafe_allow_html=True)
st.markdown(
    """
    🔹 Analyze & Score Your Resume for ATS (Applicant Tracking Systems).  
    🔹 Find matching jobs across 200+ platforms (LinkedIn, Indeed, Glassdoor, etc.).  
    🔹 Get AI-driven recommendations to improve your resume & job search.  
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# Redirect Logic using `st.query_params()`
query_params = st.query_params

if "page" in query_params:
    if query_params["page"] == "app_UI":
        st.switch_page("pages/app_UI.py")
    elif query_params["page"] == "app_ATS":
        st.switch_page("pages/app_ATS.py")

# Buttons to Redirect Users
st.markdown('<div class="button-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("📹 Tutor.AI - YouTube Summarizer", key="main_yt"):
        st.query_params["page"] = "app_UI"
        st.rerun()

with col2:
    if st.button("📄 ATS Resume Scanner & Job Finder", key="main_ats"):
        st.query_params["page"] = "app_ATS"
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">🚀 Created by Aditya Pande & Gauri Dhamale</p>', unsafe_allow_html=True)


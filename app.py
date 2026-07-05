import streamlit as st

from components.sidebar import render_sidebar

from pages.dashboard import show_dashboard
from pages.resume_analysis import show_resume_analysis
from pages.interview_prep import show_interview_prep
from pages.about import show_about


st.set_page_config(
    page_title="HireMate",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

page = render_sidebar()

if page == "Dashboard":
    show_dashboard()

elif page == "Resume Analysis":
    show_resume_analysis()

elif page == "Interview Prep":
    show_interview_prep()

else:
    show_about()
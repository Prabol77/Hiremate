import streamlit as st


def show_about():
    """
    Render About page.
    """

    st.title("About HireMate")

    st.markdown(
        """
## 💼 HireMate

HireMate is an AI-powered Resume Intelligence Platform that helps job seekers:

- Compare resumes with job descriptions
- Calculate ATS compatibility
- Identify missing skills
- Prepare for interviews
- Improve resumes using AI

**Version:** v0.3.0
"""
    )
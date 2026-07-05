import streamlit as st


def render_dashboard_header():
    """
    Dashboard Header
    """

    st.title("💼 HireMate")

    st.caption(
        "AI-Powered Resume & ATS Matching Platform"
    )

    st.markdown(
        """
Analyze your resume against a Job Description,
discover skill gaps,
and prepare for interviews.
"""
    )

    st.divider()
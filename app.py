"""
HireMate Application Entry Point.
"""

import streamlit as st

from components.layout.sidebar import render_sidebar
from styles.theme import load_theme

from views.about import show_about
from views.dashboard import show_dashboard
from views.interview_prep import show_interview_prep
from views.resume_analysis import show_resume_analysis


def main():
    """
    Configure and launch the HireMate application.
    """

    st.set_page_config(
        page_title="HireMate",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    load_theme()

    page = render_sidebar()

    if page == "Dashboard":
        show_dashboard()

    elif page == "Resume Analysis":
        show_resume_analysis()

    elif page == "Interview Prep":
        show_interview_prep()

    else:
        show_about()


if __name__ == "__main__":
    main()

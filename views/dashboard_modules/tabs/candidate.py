"""
Candidate Dashboard Tab.

Responsibilities:
- Display candidate information
- Display extracted resume preview
"""

import streamlit as st

from models.resume_model import ResumeData

from components.cards.resume_card import (
    render_resume_card,
)

from components.cards.preview_card import (
    render_preview_card,
)


# ==========================================================
# Candidate Tab
# ==========================================================


def render_candidate_tab(
    resume_data: ResumeData,
    resume_text: str,
):
    """
    Render the Candidate dashboard tab.
    """

    # ------------------------------------------------------
    # Candidate Information
    # ------------------------------------------------------

    render_resume_card(
        resume_data,
    )

    st.divider()

    # ------------------------------------------------------
    # Resume Preview
    # ------------------------------------------------------

    render_preview_card(
        resume_text,
    )

    st.divider()

    # ------------------------------------------------------
    # Resume Statistics
    # ------------------------------------------------------

    st.subheader("📋 Resume Summary")

    info = resume_data.personal_info

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Skills",
            len(resume_data.skills),
        )

    with col2:

        st.metric(
            "Projects",
            len(resume_data.projects),
        )

    with col3:

        st.metric(
            "Experience",
            len(resume_data.experience),
        )

    st.divider()

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    st.caption(
        "The information shown above has been automatically "
        "extracted from your uploaded resume."
    )
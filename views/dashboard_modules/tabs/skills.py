"""
Skills Dashboard Tab.

Responsibilities:
- Display matched skills
- Display missing skills
- Display additional skills
"""

import streamlit as st

from models.ats_model import ATSResult

from components.widgets.skills_grid import (
    render_skills_card,
)


# ==========================================================
# Skills Tab
# ==========================================================


def render_skills_tab(
    ats_result: ATSResult,
):
    """
    Render the Skills dashboard tab.
    """

    col1, col2, col3 = st.columns(3)

    # ------------------------------------------------------
    # Matched Skills
    # ------------------------------------------------------

    with col1:

        render_skills_card(
            title="Matched Skills",
            skills=ats_result.matched_skills,
            status="success",
        )

    # ------------------------------------------------------
    # Missing Skills
    # ------------------------------------------------------

    with col2:

        render_skills_card(
            title="Missing Skills",
            skills=ats_result.missing_skills,
            status="error",
        )

    # ------------------------------------------------------
    # Additional Skills
    # ------------------------------------------------------

    with col3:

        render_skills_card(
            title="Additional Skills",
            skills=ats_result.additional_skills,
            status="info",
        )

    st.divider()

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    st.caption(
        "These skills were extracted automatically by comparing "
        "your resume against the uploaded job description."
    )
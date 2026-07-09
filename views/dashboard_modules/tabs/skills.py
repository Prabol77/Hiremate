"""
Skills Dashboard Tab.

Responsibilities:
- Display matched skills
- Display missing skills
- Display skill statistics
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

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # Matched Skills
    # ------------------------------------------------------

    with col1:

        render_skills_card(
            title="✅ Matched Skills",
            skills=ats_result.matched_skills,
            status="success",
        )

    # ------------------------------------------------------
    # Missing Skills
    # ------------------------------------------------------

    with col2:

        render_skills_card(
            title="❌ Missing Skills",
            skills=ats_result.missing_skills,
            status="error",
        )

    st.divider()

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    st.subheader("📊 Skill Statistics")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Matched",
            len(ats_result.matched_skills),
        )

    with stat2:

        st.metric(
            "Missing",
            len(ats_result.missing_skills),
        )

    with stat3:

        total = (
            len(ats_result.matched_skills)
            + len(ats_result.missing_skills)
        )

        match_rate = (
            round(
                len(ats_result.matched_skills)
                / total
                * 100,
            )
            if total
            else 100
        )

        st.metric(
            "Match Rate",
            f"{match_rate}%",
        )

    st.divider()

    st.caption(
        "Skills were automatically extracted by comparing your resume with the uploaded job description."
    )
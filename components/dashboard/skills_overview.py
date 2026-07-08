"""
Dashboard Skills Overview.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def render_skills_overview(
    matched_skills: list[str],
    missing_skills: list[str],
):
    """
    Display matched and missing skills.
    """

    render_section_header(
        "🛠 Skills Analysis",
        "Skills identified from the resume and job description.",
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:

                st.success(skill)

        else:

            st.info("No matched skills found.")

    with col2:

        st.subheader("⚠ Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.warning(skill)

        else:

            st.success("No missing skills.")
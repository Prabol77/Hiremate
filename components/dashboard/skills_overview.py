"""
Dashboard Skills Overview.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _render_skill_chips(
    skills: list[str],
    color: str,
):
    if not skills:
        st.info("None")
        return

    html = '<div style="display:flex; flex-wrap:wrap; gap:8px;">'

    for skill in skills:
        html += (
            f'<span style="'
            f'background:{color};'
            f'color:white;'
            f'padding:6px 14px;'
            f'border-radius:999px;'
            f'font-size:13px;'
            f'font-weight:600;'
            f'white-space:nowrap;'
            f'display:inline-block;'
            f'">'
            f'{skill}'
            f'</span>'
        )

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True,
    )
# ==========================================================
# Skills Overview
# ==========================================================


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

    left, right = st.columns(2)

    with left:

        st.subheader(
            "✅ Matched Skills"
        )

        _render_skill_chips(
            matched_skills,
            "#16a34a",
        )

    with right:

        st.subheader(
            "⚠ Missing Skills"
        )

        _render_skill_chips(
            missing_skills,
            "#d97706",
        )
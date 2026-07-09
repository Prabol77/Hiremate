"""
ATS Score Breakdown.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _progress(
    title: str,
    score: float,
):

    st.write(f"**{title}**")

    st.progress(
        score / 100,
    )

    st.caption(
        f"{score:.0f}%"
    )


def render_ats_breakdown(
    ats_result,
):
    """
    Display detailed ATS score breakdown.
    """

    render_section_header(
        "📊 ATS Breakdown",
        "Detailed scoring across all evaluation categories.",
    )

    _progress(
        "🎯 Skills Match",
        ats_result.skills_score,
    )

    _progress(
        "🚀 Projects",
        ats_result.projects_score,
    )

    _progress(
        "💼 Experience",
        ats_result.experience_score,
    )

    _progress(
        "🎓 Education",
        ats_result.education_score,
    )

    _progress(
        "📄 Resume Completeness",
        ats_result.completeness_score,
    )
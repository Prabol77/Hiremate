"""
Dashboard ATS Metrics.
"""

import streamlit as st

from components.ui.metric_card import (
    render_metric_card,
)

from components.ui.section_header import (
    render_section_header,
)


def render_ats_metrics(
    ats_score: float,
    matched_skills: int,
    missing_skills: int,
    resume_quality: str,
):
    """
    Render dashboard metrics.
    """

    render_section_header(
        "📊 Resume Analytics",
        "Overall performance of your resume.",
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_metric_card(
            title="ATS Score",
            value=f"{ats_score:.1f}%",
            help_text="Overall ATS compatibility.",
        )

    with col2:

        render_metric_card(
            title="Matched",
            value=matched_skills,
            help_text="Skills matched with the job description.",
        )

    with col3:

        render_metric_card(
            title="Missing",
            value=missing_skills,
            help_text="Skills missing from the resume.",
        )

    with col4:

        render_metric_card(
            title="Quality",
            value=resume_quality,
            help_text="Overall resume quality.",
        )
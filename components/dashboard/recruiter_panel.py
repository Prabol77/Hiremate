"""
Recruiter Assessment Panel.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def render_recruiter_panel(
    resume_data,
    ats_result,
):
    """
    Render recruiter assessment.
    """

    render_section_header(
        "👔 Recruiter Assessment",
        "AI-generated hiring recommendation based on resume analysis.",
    )

    # =====================================================
    # Decision
    # =====================================================

    score = ats_result.overall_score

    if score >= 85:

        decision = "✅ Shortlist"

    elif score >= 70:

        decision = "🟡 Consider"

    else:

        decision = "❌ Reject"

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Decision",
            decision,
        )

    with col2:

        st.metric(
            "ATS Score",
            f"{score:.0f}%",
        )

    st.divider()

    # =====================================================
    # Candidate Snapshot
    # =====================================================

    meta = resume_data.metadata

    st.subheader("📋 Candidate Snapshot")

    st.write(
        f"**Primary Domain:** {meta.get('primary_domain','General')}"
    )

    st.write(
        f"**Projects:** {meta.get('project_count',0)}"
    )

    st.write(
        f"**Experience Entries:** {meta.get('experience_count',0)}"
    )

    st.write(
        f"**Skills:** {meta.get('skill_count',0)}"
    )

    st.divider()

    # =====================================================
    # Strengths
    # =====================================================

    st.subheader("💪 Strengths")

    if ats_result.strengths:

        for item in ats_result.strengths:

            st.success(item)

    else:

        st.info(
            "No major strengths detected."
        )

    # =====================================================
    # Concerns
    # =====================================================

    st.subheader("⚠ Concerns")

    if ats_result.weaknesses:

        for item in ats_result.weaknesses:

            st.warning(item)

    else:

        st.success(
            "No significant concerns."
        )

    # =====================================================
    # Recommendation
    # =====================================================

    st.subheader("📌 Recommendation")

    if decision == "✅ Shortlist":

        st.success(
            "Proceed to the Technical Interview round."
        )

    elif decision == "🟡 Consider":

        st.info(
            "Suitable candidate with a few improvement areas."
        )

    else:

        st.error(
            "Resume needs significant improvement before proceeding."
        )
"""
Career Coach Dashboard Card.
"""

import streamlit as st


# ==========================================================
# Helper
# ==========================================================

def _render_list(
    title: str,
    items: list[str],
    icon: str,
):
    """
    Render a simple bullet list.
    """

    st.subheader(
        f"{icon} {title}"
    )

    if not items:

        st.info(
            "No information available."
        )

        return

    for item in items:

        st.markdown(
            f"- {item}"
        )


# ==========================================================
# Career Coach
# ==========================================================

def render_career_coach_card(
    coach,
):
    """
    Render AI Career Coach.
    """

    st.subheader(
        "🧠 AI Career Coach"
    )

    # ======================================================
    # Summary
    # ======================================================

    st.info(
        coach.summary,
    )

    st.divider()

    # ======================================================
    # Strengths / Focus Areas
    # ======================================================

    left, right = st.columns(2)

    with left:

        _render_list(
            "Strengths",
            coach.strengths,
            "💪",
        )

    with right:

        _render_list(
            "Focus Areas",
            coach.focus_areas,
            "🎯",
        )

    st.divider()

    # ======================================================
    # Weekly Goals
    # ======================================================

    _render_list(
        "Weekly Goals",
        coach.weekly_goals,
        "📅",
    )

    st.divider()

    # ======================================================
    # Recommended Projects
    # ======================================================

    _render_list(
        "Recommended Projects",
        coach.recommended_projects,
        "🚀",
    )

    st.divider()

    # ======================================================
    # Certifications
    # ======================================================

    _render_list(
        "Recommended Certifications",
        coach.recommended_certifications,
        "📜",
    )

    st.divider()

    # ======================================================
    # Interview Strategy
    # ======================================================

    _render_list(
        "Interview Strategy",
        coach.interview_strategy,
        "🎤",
    )

    st.divider()

    # ======================================================
    # Motivation
    # ======================================================

    st.success(
        coach.final_message,
    )
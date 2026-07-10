"""
Career Intelligence Summary Card.
"""

import streamlit as st


def _render_list(title, items, icon):
    st.subheader(f"{icon} {title}")

    if not items:
        st.info("No items available.")
        return

    for item in items:
        st.markdown(f"- {item}")


def render_career_summary(career):
    """
    Render the Career Intelligence summary.
    """

    st.subheader("🚀 Career Intelligence")

    # =====================================================
    # Hero Metrics
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Career Stage",
            career.stage,
        )

    with col2:
        st.metric(
            "Readiness",
            f"{career.readiness_score}%",
        )

    st.progress(career.readiness_score / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Confidence",
            career.confidence,
        )

    with col2:
        st.metric(
            "Learning Duration",
            career.estimated_duration,
        )

    st.divider()

    # =====================================================
    # Summary
    # =====================================================

    st.info(career.summary)

    st.divider()

    # =====================================================
    # Strengths / Improvements
    # =====================================================

    left, right = st.columns(2)

    with left:
        _render_list(
            "Top Strengths",
            career.strengths,
            "💪",
        )

    with right:
        _render_list(
            "Improvement Areas",
            career.improvement_areas,
            "🎯",
        )

    st.divider()

    # =====================================================
    # Next Steps
    # =====================================================

    _render_list(
        "Next Learning Steps",
        career.next_steps,
        "➡",
    )
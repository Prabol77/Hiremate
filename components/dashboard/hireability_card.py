"""
Hireability Dashboard Card.
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

    st.subheader(f"{icon} {title}")

    if not items:

        st.info("Nothing to display.")

        return

    for item in items:

        st.markdown(f"- {item}")


# ==========================================================
# Main Card
# ==========================================================

def render_hireability_card(
    hireability,
):
    """
    Render Hireability Intelligence Dashboard.
    """

    st.subheader(
        "🏆 Hireability Intelligence"
    )

    # ======================================================
    # Hero Metrics
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Hireability",
            f"{hireability.overall}%",
        )

    with col2:

        st.metric(
            "Grade",
            hireability.grade,
        )

    st.progress(
        hireability.overall / 100,
    )

    st.success(
        f"Potential Improvement: +{hireability.improvement_potential}%"
    )

    st.divider()

    # ======================================================
    # Breakdown
    # ======================================================

    left, right = st.columns(2)

    with left:

        st.metric(
            "Resume",
            f"{hireability.resume}%",
        )

        st.metric(
            "Technical",
            f"{hireability.technical}%",
        )

        st.metric(
            "Career",
            f"{hireability.career}%",
        )

    with right:

        st.metric(
            "ATS",
            f"{hireability.ats}%",
        )

        st.metric(
            "Projects",
            f"{hireability.projects}%",
        )

        st.metric(
            "Interview",
            f"{hireability.interview}%",
        )

    st.divider()

    # ======================================================
    # Insights
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        _render_list(
            "Top Strengths",
            hireability.strengths,
            "💪",
        )

    with col2:

        _render_list(
            "Focus Areas",
            hireability.weaknesses,
            "⚠",
        )

    st.divider()

    # ======================================================
    # Next Actions
    # ======================================================

    _render_list(
        "Next Actions",
        hireability.next_actions,
        "🚀",
    )
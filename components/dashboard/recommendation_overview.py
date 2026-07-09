"""
Recommendation Overview.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _render_section(
    title: str,
    items: list[str],
):

    st.subheader(title)

    if not items:

        st.info("No recommendations.")

        return

    for item in items:

        st.markdown(f"• {item}")


def render_recommendation_overview(
    recommendation,
):
    """
    Render recommendation overview.
    """

    render_section_header(
        "💡 Career Roadmap",
        "Personalized recommendations to improve your profile.",
    )

    _render_section(
        "🚀 Technical",
        recommendation.technical,
    )

    st.divider()

    _render_section(
        "📄 Resume",
        recommendation.resume,
    )

    st.divider()

    _render_section(
        "💼 Career",
        recommendation.career,
    )
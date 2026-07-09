"""
Recommendation Details.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _section(title, items):

    st.subheader(title)

    if not items:
        st.info("No recommendations.")
        return

    for item in items:
        st.markdown(f"• {item}")

    st.divider()


def render_recommendation_details(recommendation):

    render_section_header(
        "💡 Career Roadmap",
        "Personalized recommendations.",
    )

    _section(
        "🚀 Technical",
        recommendation.technical,
    )

    _section(
        "📄 Resume",
        recommendation.resume,
    )

    _section(
        "💼 Career",
        recommendation.career,
    )
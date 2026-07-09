"""
Review Details.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _render_list(title: str, items: list[str], icon: str):

    st.subheader(f"{icon} {title}")

    if not items:
        st.info("Nothing to display.")
        return

    for item in items:
        st.markdown(f"• {item}")

    st.divider()


def render_review_details(review):
    """
    Render detailed AI review.
    """

    render_section_header(
        "📝 Resume Review",
        "AI-generated review of the uploaded resume.",
    )

    st.subheader("📄 Summary")

    st.write(review.summary)

    st.divider()

    _render_list(
        "Strengths",
        review.strengths,
        "💪",
    )

    _render_list(
        "Weaknesses",
        review.weaknesses,
        "⚠",
    )

    _render_list(
        "Recommendations",
        review.recommendations,
        "💡",
    )
"""
Review Dashboard Tab.

Responsibilities:
- Display AI-generated resume review
"""

import streamlit as st

from models.review_model import ReviewResult

from components.cards.review_card import (
    render_review_card,
)


# ==========================================================
# Review Tab
# ==========================================================


def render_review_tab(
    review: ReviewResult,
):
    """
    Render the AI Resume Review dashboard tab.
    """

    render_review_card(
        review,
    )

    st.divider()

    if review.summary:

        st.success(
            "AI review generated successfully."
        )

    else:

        st.warning(
            "No review was generated."
        )

    st.caption(
        "The review is generated using AI by comparing your "
        "resume against the uploaded job description."
    )
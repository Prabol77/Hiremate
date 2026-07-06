import streamlit as st

from models.review_model import ReviewResult


def render_review_card(
    review: ReviewResult,
) -> None:
    """
    Render the AI Resume Review section.

    Args:
        review:
            AI-generated review results.
    """

    st.header("🤖 AI Resume Review")

    # =====================================================
    # Summary
    # =====================================================

    st.info(review.summary or "No review summary available.")

    # =====================================================
    # Strengths & Weaknesses
    # =====================================================

    col1, col2 = st.columns(2)

    review_sections = [
        (
            col1,
            "💪 Strengths",
            review.strengths,
            st.success,
            "No strengths detected.",
            st.warning,
        ),
        (
            col2,
            "⚠️ Weaknesses",
            review.weaknesses,
            st.error,
            "No weaknesses detected.",
            st.success,
        ),
    ]

    for (
        column,
        title,
        items,
        render_item,
        empty_message,
        render_empty,
    ) in review_sections:

        with column:

            st.subheader(title)

            if items:

                for item in items:

                    render_item(item)

            else:

                render_empty(empty_message)

    # =====================================================
    # Recommendations
    # =====================================================

    st.divider()

    st.subheader("📈 Recommendations")

    if review.recommendations:

        for recommendation in review.recommendations:

            st.markdown(f"- {recommendation}")

    else:

        st.success("Your resume is already well optimized.")

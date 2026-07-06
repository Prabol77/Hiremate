import streamlit as st

from models.review_model import ReviewResult


def render_review_card(
    review: ReviewResult,
):
    """
    Render AI Resume Review.
    """

    st.header("🤖 AI Resume Review")

    st.info(
        review.summary
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💪 Strengths")

        if review.strengths:

            for item in review.strengths:

                st.success(item)

        else:

            st.warning("No strengths detected.")

    with col2:

        st.subheader("⚠ Weaknesses")

        if review.weaknesses:

            for item in review.weaknesses:

                st.error(item)

        else:

            st.success("No weaknesses detected.")

    st.divider()

    st.subheader("📈 Recommendations")

    if review.recommendations:

        for recommendation in review.recommendations:

            st.write(
                f"• {recommendation}"
            )

    else:

        st.success(
            "Your resume is already well optimized."
        )
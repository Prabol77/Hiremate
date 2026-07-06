import streamlit as st

from models.recommendation_model import RecommendationResult


def render_recommendation_card(
    recommendations: RecommendationResult,
):
    """
    Render AI recommendations.
    """

    st.header("💡 AI Recommendations")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🛠 Technical")

        for item in recommendations.technical:

            st.info(item)

    with col2:

        st.subheader("📄 Resume")

        for item in recommendations.resume:

            st.success(item)

    with col3:

        st.subheader("🚀 Career")

        for item in recommendations.career:

            st.warning(item)
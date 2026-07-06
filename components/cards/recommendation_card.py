import streamlit as st

from models.recommendation_model import RecommendationResult


def render_recommendation_card(
    recommendation: RecommendationResult,
) -> None:
    """
    Render AI-powered career recommendations.

    Args:
        recommendation:
            AI-generated recommendation results.
    """

    st.header("🎯 AI Career Recommendations")

    sections = [
        (
            "🎯 ATS Optimization",
            recommendation.ats_optimization,
            st.success,
        ),
        (
            "📚 Skills to Learn",
            recommendation.skills_to_learn,
            st.info,
        ),
        (
            "📝 Resume Improvements",
            recommendation.resume_improvements,
            st.warning,
        ),
        (
            "🚀 Next Steps",
            recommendation.next_steps,
            st.success,
        ),
    ]

    for (
        title,
        items,
        render_function,
    ) in sections:

        with st.expander(
            title,
            expanded=True,
        ):

            if items:

                for item in items:

                    render_function(item)

            else:

                st.info("No recommendations available.")

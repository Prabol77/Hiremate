"""
Dashboard Recommendation Overview.
"""

import streamlit as st

from models.recommendation_model import (
    RecommendationResult,
)

from components.ui.section_header import (
    render_section_header,
)


def render_recommendation_overview(
    recommendation: RecommendationResult,
):
    """
    Display recommendation preview.
    """

    render_section_header(
        "💡 Recommendations",
        "Top improvements suggested by HireMate AI.",
    )

    for item in recommendation.resume_improvements[:5]:

        st.success(item)
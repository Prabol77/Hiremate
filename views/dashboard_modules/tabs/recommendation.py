"""
Recommendation Tab.
"""

from models.recommendation_model import (
    RecommendationResult,
)

from components.dashboard.recommendation_details import (
    render_recommendation_details,
)


def render_recommendation_tab(
    recommendation: RecommendationResult,
):
    """
    Render recommendation tab.
    """

    render_recommendation_details(
        recommendation,
    )
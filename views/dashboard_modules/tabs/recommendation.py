"""
Recommendation Dashboard.
"""

from components.dashboard.recommendation_details import (
    render_recommendation_details,
)


def render_recommendation_tab(recommendation):

    render_recommendation_details(
        recommendation,
    )
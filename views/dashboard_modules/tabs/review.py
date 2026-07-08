"""
Review Tab.
"""

from models.review_model import ReviewResult

from components.dashboard.review_details import (
    render_review_details,
)


def render_review_tab(
    review: ReviewResult,
):
    """
    Render AI review tab.
    """

    render_review_details(
        review,
    )
"""
Dashboard Recommendation Details.
"""

import streamlit as st

from models.recommendation_model import (
    RecommendationResult,
)

from components.ui.section_header import (
    render_section_header,
)

from components.ui.status_badge import (
    render_status_badge,
)


def _render_list(
    title: str,
    items: list[str],
    status: str,
    empty_message: str,
):
    """
    Render a recommendation list.
    """

    st.subheader(title)

    if items:

        for item in items:

            render_status_badge(
                status,
                item,
            )

    else:

        render_status_badge(
            "info",
            empty_message,
        )

    st.divider()


def render_recommendation_details(
    recommendation: RecommendationResult,
):
    """
    Render complete recommendation details.
    """

    render_section_header(
        "💡 AI Recommendations",
        "Actionable improvements suggested by HireMate AI.",
    )

    _render_list(
        "📄 Resume Improvements",
        recommendation.resume_improvements,
        "success",
        "No resume improvements suggested.",
    )

    _render_list(
        "🛠 Skills To Learn",
        recommendation.skills_to_learn,
        "warning",
        "No additional skills suggested.",
    )

    _render_list(
        "⚙ ATS Optimization",
        recommendation.ats_optimization,
        "info",
        "Resume is ATS optimized.",
    )

    _render_list(
        "🚀 Next Steps",
        recommendation.next_steps,
        "success",
        "No additional next steps.",
    )
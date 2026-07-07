"""
HireMate Dashboard

Main dashboard entry point.

Responsibilities:
- Render hero section
- Handle file upload
- Execute analysis
- Render dashboard tabs
- Handle errors
"""

import streamlit as st

from components.layout.hero_section import render_hero_section
from components.widgets.empty_state import render_empty_state
from components.widgets.error_card import render_error_card

from views.dashboard_modules.upload import (
    render_upload_section,
)

from views.dashboard_modules.analysis import (
    get_cached_analysis,
)

from views.dashboard_modules.tabs.overview import (
    render_overview_tab,
)

from views.dashboard_modules.tabs.skills import (
    render_skills_tab,
)

from views.dashboard_modules.tabs.review import (
    render_review_tab,
)

from views.dashboard_modules.tabs.recommendation import (
    render_recommendation_tab,
)

from views.dashboard_modules.tabs.interview import (
    render_interview_tab,
)

from views.dashboard_modules.tabs.rewrite import (
    render_rewrite_tab,
)

from views.dashboard_modules.tabs.candidate import (
    render_candidate_tab,
)

from services.session_service import SessionService


# ==========================================================
# Dashboard
# ==========================================================


def show_dashboard():
    """
    Render the main HireMate dashboard.
    """

    render_hero_section()

    resume, jd = render_upload_section()

    if not (resume and jd):

        render_empty_state()

        return

    try:

        analysis = get_cached_analysis(
            resume,
            jd,
        )

        (
            resume_pdf,
            resume_text,
            jd_text,
            resume_data,
            job_data,
            ats_result,
            review,
            recommendations,
            interview,
        ) = analysis

        if st.button(
            "🔄 Start New Analysis",
            use_container_width=True,
        ):

            SessionService().clear()

            st.session_state.pop(
                "resume",
                None,
            )

            st.session_state.pop(
                "jd",
                None,
            )

            st.rerun()

        (
            overview_tab,
            skills_tab,
            review_tab,
            recommendation_tab,
            interview_tab,
            rewrite_tab,
            candidate_tab,
        ) = st.tabs(
            [
                "📊 Overview",
                "🛠 Skills",
                "🤖 AI Review",
                "💡 Recommendations",
                "🎤 Interview",
                "✨ Rewrite",
                "👤 Candidate",
            ]
        )

        with overview_tab:

            render_overview_tab(
                resume_pdf,
                resume_data,
                ats_result,
                review,
                recommendations,
                interview,
            )

        with skills_tab:

            render_skills_tab(
                ats_result,
            )

        with review_tab:

            render_review_tab(
                review,
            )

        with recommendation_tab:

            render_recommendation_tab(
                recommendations,
            )

        with interview_tab:

            render_interview_tab(
                interview,
            )

        with rewrite_tab:

            render_rewrite_tab(
                resume_data,
                jd_text,
            )

        with candidate_tab:

            render_candidate_tab(
                resume_data,
                resume_text,
            )

    except Exception as error:

        render_error_card(
            error,
        )
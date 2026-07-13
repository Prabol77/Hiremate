"""
HireMate Dashboard

Main dashboard entry point.

Responsibilities
----------------
- Render Hero Section
- Handle File Upload
- Execute Resume Analysis
- Render Dashboard Workspaces
- Handle Errors
"""

import streamlit as st
from views.dashboard_modules.tabs.rewrite import (
    render_rewrite_tab,
)
from components.layout.hero_section import (
    render_hero_section,
)

from components.widgets.empty_state import (
    render_empty_state,
)

from components.widgets.error_card import (
    render_error_card,
)

from services.session_service import (
    SessionService,
)

from views.dashboard_modules.upload import (
    render_upload_section,
)

from views.dashboard_modules.analysis import (
    get_cached_analysis,
)

from views.dashboard_modules.tabs.overview import (
    render_overview_tab,
)

from views.dashboard_modules.tabs.resume import (
    render_resume_tab,
)

from views.dashboard_modules.tabs.career import (
    render_career_tab,
)

from views.dashboard_modules.tabs.interview import (
    render_interview_tab,
)

from views.dashboard_modules.tabs.documents import (
    render_documents_tab,
)


# ==========================================================
# Dashboard
# ==========================================================


def show_dashboard():
    """
    Render the HireMate Dashboard.
    """

    # ======================================================
    # Hero Section
    # ======================================================

    render_hero_section()

    # ======================================================
    # Upload Section
    # ======================================================

    resume, jd = render_upload_section()

    if not (resume and jd):

        render_empty_state()

        return

    # ======================================================
    # Analysis
    # ======================================================

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
            skill_gap,
            roadmap,
            career,
            hireability,
            projects,
            career_coach,
            company_matches,
            certifications,
            personalization,
            review,
            recommendations,
            interview,
            cover_letter,
            rewrite,
        ) = analysis

        # ==================================================
        # Start New Analysis
        # ==================================================

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

        # ==================================================
        # Dashboard Workspaces
        # ==================================================

        (
            dashboard_tab,
            resume_tab,
            rewrite_tab,
            career_tab,
            interview_tab,
            documents_tab,
        ) = st.tabs(
            [
                "🏠 Dashboard",
                "👤 Resume",
                "✨ Rewrite",
                "🚀 Career",
                "🎤 Interview",
                "📄 Documents",
            ]
        )

        # ==================================================
        # Dashboard Workspace
        # ==================================================

        with dashboard_tab:

            render_overview_tab(
                resume_pdf,
                resume_data,
                ats_result,
                hireability,
                review,
                recommendations,
                interview,
                cover_letter,
            )

        # ==================================================
        # Resume Workspace
        # ==================================================

        with resume_tab:

            render_resume_tab(
                resume_data,
                resume_text,
                ats_result,
                review,
            )

        # ==================================================
        # Rewrite Workspace
        # ==================================================

        with rewrite_tab:
            render_rewrite_tab(
                rewrite,
            )

        # ==================================================
        # Career Workspace
        # ==================================================

        with career_tab:

            render_career_tab(
                career,
                hireability,
                career_coach,
                projects,
                company_matches,
                certifications,
                personalization,
                skill_gap,
                roadmap,
            )

        # ==================================================
        # Interview Workspace
        # ==================================================

        with interview_tab:

            render_interview_tab(
                interview,
            )

        # ==================================================
        # Documents Workspace
        # ==================================================

        with documents_tab:

            render_documents_tab(
                cover_letter,
            )

    # ======================================================
    # Error Handling
    # ======================================================

    except Exception as error:

        render_error_card(
            error,
        )
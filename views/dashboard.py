import streamlit as st

from config import (
    SUPPORTED_JD_TYPES,
    SUPPORTED_RESUME_TYPES,
)

from components.layout.hero_section import render_hero_section

from components.cards.statistics_card import render_statistics_card
from components.cards.ats_card import render_ats_card
from components.cards.summary_card import render_summary_card
from components.cards.resume_card import render_resume_card
from components.cards.review_card import render_review_card
from components.cards.recommendation_card import (
    render_recommendation_card,
)
from components.cards.interview_card import (
    render_interview_card,
)

from components.widgets.resume_preview import render_preview_card
from components.widgets.skills_grid import render_skills_card

from components.charts.gauge_chart import render_gauge
from components.charts.skill_chart import render_skill_chart

from components.uploader import save_uploaded_file

from services.analysis_service import AnalysisService

from utils.parser import extract_pdf_data


def show_dashboard():
    """
    Render HireMate Dashboard.
    """

    render_hero_section()

    upload_col1, upload_col2 = st.columns(2)

    with upload_col1:

        resume = st.file_uploader(
            "📄 Upload Resume",
            type=SUPPORTED_RESUME_TYPES,
            key="resume",
        )

    with upload_col2:

        jd = st.file_uploader(
            "💼 Upload Job Description",
            type=SUPPORTED_JD_TYPES,
            key="jd",
        )

    if not (resume and jd):

        st.info(
            "Upload both Resume and Job Description to begin analysis."
        )

        return

    try:

        with st.spinner(
            "Analyzing Resume..."
        ):

            # =====================================
            # Save Uploaded Files
            # =====================================

            resume_path = save_uploaded_file(
                resume
            )

            jd_path = save_uploaded_file(
                jd
            )

            # =====================================
            # Extract Resume
            # =====================================

            resume_pdf = extract_pdf_data(
                resume_path
            )

            resume_text = resume_pdf["text"]

            # =====================================
            # Extract JD
            # =====================================

            if jd.name.lower().endswith(".pdf"):

                jd_pdf = extract_pdf_data(
                    jd_path
                )

                jd_text = jd_pdf["text"]

            else:

                with open(
                    jd_path,
                    "r",
                    encoding="utf-8",
                ) as file:

                    jd_text = file.read()

            # =====================================
            # Complete Analysis Pipeline
            # =====================================

            analysis = AnalysisService()

            (
                resume_data,
                job_data,
                ats_result,
                review,
                recommendations,
                interview,
            ) = analysis.analyze(
                resume_text,
                jd_text,
            )

        st.success(
            "✅ Analysis completed successfully."
        )

        (
            overview_tab,
            skills_tab,
            review_tab,
            recommendation_tab,
            interview_tab,
            candidate_tab,
        ) = st.tabs(
            [
                "📊 Overview",
                "🛠 Skills",
                "🤖 AI Review",
                "💡 Recommendations",
                "🎤 Interview",
                "👤 Candidate",
            ]
        )

        # =====================================================
        # OVERVIEW
        # =====================================================

        with overview_tab:

            left, right = st.columns(2)

            with left:

                render_statistics_card(
                    resume_pdf
                )

            with right:

                render_ats_card(
                    ats_result.overall_score
                )

            st.divider()

            render_summary_card(
                ats_result
            )

            st.divider()

            chart_left, chart_right = st.columns(2)

            with chart_left:

                render_gauge(
                    ats_result.overall_score
                )

            with chart_right:

                render_skill_chart(
                    ats_result
                )

        # =====================================================
        # SKILLS
        # =====================================================

        with skills_tab:

            col1, col2, col3 = st.columns(3)

            with col1:

                render_skills_card(
                    "Matched Skills",
                    ats_result.matched_skills,
                    "success",
                )

            with col2:

                render_skills_card(
                    "Missing Skills",
                    ats_result.missing_skills,
                    "error",
                )

            with col3:

                render_skills_card(
                    "Additional Skills",
                    ats_result.additional_skills,
                    "info",
                )

        # =====================================================
        # AI REVIEW
        # =====================================================

        with review_tab:

            render_review_card(
                review
            )

        # =====================================================
        # RECOMMENDATIONS
        # =====================================================

        with recommendation_tab:

            render_recommendation_card(
                recommendations
            )

        # =====================================================
        # INTERVIEW QUESTIONS
        # =====================================================

        with interview_tab:

            render_interview_card(
                interview
            )

        # =====================================================
        # CANDIDATE
        # =====================================================

        with candidate_tab:

            render_resume_card(
                resume_data
            )

            st.divider()

            render_preview_card(
                resume_text
            )

    except Exception as error:

        st.error(
            "❌ Failed to analyze the uploaded documents."
        )

        st.exception(error)
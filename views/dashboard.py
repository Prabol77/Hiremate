import streamlit as st

from components.cards.ats_card import render_ats_card
from components.cards.interview_card import render_interview_card
from components.cards.recommendation_card import render_recommendation_card
from components.cards.resume_card import render_resume_card
from components.cards.review_card import render_review_card
from components.cards.statistics_card import render_statistics_card
from components.cards.summary_card import render_summary_card
from components.charts.gauge_chart import render_gauge
from components.charts.skill_chart import render_skill_chart
from components.export_button import render_export_button
from components.layout.hero_section import render_hero_section
from components.uploader import save_uploaded_file
from components.widgets.empty_state import render_empty_state
from components.widgets.error_card import render_error_card
from components.widgets.progress_pipeline import ProgressPipeline
from components.widgets.resume_preview import render_preview_card
from components.widgets.skills_grid import render_skills_card
from config import SUPPORTED_JD_TYPES, SUPPORTED_RESUME_TYPES
from services.analysis_service import AnalysisService
from services.session_service import SessionService
from utils.parser import extract_pdf_data

# ==========================================================
# Upload Section
# ==========================================================


def render_upload_section():

    left, right = st.columns(2)

    with left:

        resume = st.file_uploader(
            "📄 Upload Resume",
            type=SUPPORTED_RESUME_TYPES,
            key="resume",
        )

    with right:

        jd = st.file_uploader(
            "💼 Upload Job Description",
            type=SUPPORTED_JD_TYPES,
            key="jd",
        )

    return resume, jd


# ==========================================================
# Load Uploaded Documents
# ==========================================================


def load_documents(
    resume,
    jd,
):

    resume.seek(0)
    jd.seek(0)

    resume_path = save_uploaded_file(
        resume,
    )

    jd_path = save_uploaded_file(
        jd,
    )

    resume_pdf = extract_pdf_data(
        resume_path,
    )

    resume_text = resume_pdf["text"]

    if jd.name.lower().endswith(".pdf"):

        jd_pdf = extract_pdf_data(
            jd_path,
        )

        jd_text = jd_pdf["text"]

    else:

        with open(
            jd_path,
            "r",
            encoding="utf-8",
        ) as file:

            jd_text = file.read()

    return (
        resume_pdf,
        resume_text,
        jd_text,
    )


# ==========================================================
# Cached Analysis
# ==========================================================


def get_cached_analysis(
    resume,
    jd,
):

    session = SessionService()

    pipeline = ProgressPipeline()

    resume_bytes = resume.getvalue()

    jd_bytes = jd.getvalue()

    file_hash = session.generate_hash(
        resume_bytes,
        jd_bytes,
    )

    if session.has_cached_analysis(
        file_hash,
    ):

        pipeline.update(
            100,
            "⚡ Loaded cached analysis.",
        )

        return session.get_analysis()

    pipeline.update(
        10,
        "📄 Reading Resume...",
    )

    (
        resume_pdf,
        resume_text,
        jd_text,
    ) = load_documents(
        resume,
        jd,
    )

    pipeline.update(
        30,
        "📑 Parsing Documents...",
    )

    analysis = AnalysisService()

    pipeline.update(
        55,
        "🎯 Running ATS Analysis...",
    )

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

    pipeline.update(
        90,
        "🤖 Generating AI Insights...",
    )

    pipeline.finish()

    result = (
        resume_pdf,
        resume_text,
        resume_data,
        job_data,
        ats_result,
        review,
        recommendations,
        interview,
    )

    session.save_analysis(
        file_hash,
        result,
    )

    return result


# ==========================================================
# Dashboard
# ==========================================================


def show_dashboard():

    render_hero_section()

    resume, jd = render_upload_section()

    if not (resume and jd):

        render_empty_state()

        return

    try:

        (
            resume_pdf,
            resume_text,
            resume_data,
            job_data,
            ats_result,
            review,
            recommendations,
            interview,
        ) = get_cached_analysis(
            resume,
            jd,
        )
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

        # ==========================================================
        # OVERVIEW
        # ==========================================================

        with overview_tab:

            left, right = st.columns(2)

            with left:

                render_statistics_card(
                    resume_pdf,
                )

            with right:

                render_ats_card(
                    ats_result.overall_score,
                )

            st.divider()

            render_summary_card(
                ats_result,
            )

            st.divider()

            chart_left, chart_right = st.columns(2)

            with chart_left:

                render_gauge(
                    ats_result.overall_score,
                )

            with chart_right:

                render_skill_chart(
                    ats_result,
                )

            st.divider()

            render_export_button(
                resume_data,
                ats_result,
                review,
                recommendations,
                interview,
            )

        # ==========================================================
        # SKILLS
        # ==========================================================

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

            st.divider()

        # ==========================================================
        # AI REVIEW
        # ==========================================================

        with review_tab:

            render_review_card(
                review,
            )

            if review.summary:

                st.divider()

                st.info("AI review completed successfully.")
        # ==========================================================
        # RECOMMENDATIONS
        # ==========================================================

        with recommendation_tab:

            render_recommendation_card(
                recommendations,
            )

            st.divider()

            st.caption(
                "These recommendations are generated based on the uploaded resume and job description."
            )

        # ==========================================================
        # INTERVIEW
        # ==========================================================

        with interview_tab:

            render_interview_card(
                interview,
            )

            st.divider()

            st.caption("Practice these questions before applying.")

        # ==========================================================
        # CANDIDATE
        # ==========================================================

        with candidate_tab:

            render_resume_card(
                resume_data,
            )

            st.divider()

            st.subheader("📄 Resume Preview")

            render_preview_card(
                resume_text,
            )

    except Exception as e:

        render_error_card(
            e,
        )

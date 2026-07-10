"""
Dashboard Analysis Module.

Responsibilities:
- Execute resume analysis
- Manage session cache
- Manage progress pipeline
"""

from services.analysis_service import AnalysisService
from services.session_service import SessionService

from components.widgets.progress_pipeline import (
    ProgressPipeline,
)

from views.dashboard_modules.upload import (
    load_documents,
)


# ==========================================================
# Cached Analysis
# ==========================================================


def get_cached_analysis(
    resume,
    jd,
):
    """
    Run or retrieve cached analysis.

    Returns:

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
        review,
        recommendations,
        interview,
        cover_letter,
    )
    """

    session = SessionService()

    pipeline = ProgressPipeline()

    resume_bytes = resume.getvalue()

    jd_bytes = jd.getvalue()

    file_hash = session.generate_hash(
        resume_bytes,
        jd_bytes,
    )

    # ======================================================
    # Cached Analysis
    # ======================================================

    if session.has_cached_analysis(
        file_hash,
    ):

        pipeline.finish()

        return session.get_analysis()

    # ======================================================
    # Read Documents
    # ======================================================

    pipeline.update(
        10,
        "📄 Reading uploaded documents...",
    )

    (
        resume_pdf,
        resume_text,
        jd_text,
    ) = load_documents(
        resume,
        jd,
    )

    # ======================================================
    # Analysis
    # ======================================================

    analysis = AnalysisService()

    pipeline.update(
        35,
        "📑 Parsing resume and job description...",
    )

    (
        resume_data,
        job_data,
        ats_result,
        skill_gap,
        roadmap,
        career,
        review,
        recommendations,
        interview,
        cover_letter,
    ) = analysis.analyze(
        resume_text,
        jd_text,
    )

    pipeline.update(
        80,
        "🤖 Generating AI insights...",
    )

    # ======================================================
    # Final Result
    # ======================================================

    result = (
        resume_pdf,
        resume_text,
        jd_text,
        resume_data,
        job_data,
        ats_result,
        skill_gap,
        roadmap,
        career,
        review,
        recommendations,
        interview,
        cover_letter,
    )

    session.save_analysis(
        file_hash,
        result,
    )

    pipeline.finish()

    return result
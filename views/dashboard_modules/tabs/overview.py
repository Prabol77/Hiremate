"""
HireMate Overview Dashboard.

Responsibilities:
- ATS Metrics
- Resume Summary
- Skills Overview
- AI Review Preview
- Recommendation Preview
- Export Report
"""
# from components.dashboard.export_report import (
#     render_export_report,
# )
from components.dashboard.ats_metrics import (
    render_ats_metrics,
)

from components.dashboard.summary_card import (
    render_summary_card,
)

from components.dashboard.skills_overview import (
    render_skills_overview,
)

from components.dashboard.review_overview import (
    render_review_overview,
)

from components.dashboard.recommendation_overview import (
    render_recommendation_overview,
)

from components.dashboard.export_report import (
    render_export_report,
)


def render_overview_tab(
    resume_pdf,
    resume_data,
    ats_result,
    review,
    recommendations,
    interview,
    cover_letter,
):
    """
    Render the HireMate Overview Dashboard.
    """

    # ======================================================
    # ATS Metrics
    # ======================================================

    render_ats_metrics(

        ats_score=ats_result.overall_score,

        matched_skills=len(
            ats_result.matched_skills,
        ),

        missing_skills=len(
            ats_result.missing_skills,
        ),

        resume_quality=(
            "Excellent"
            if ats_result.overall_score >= 85
            else
            "Good"
            if ats_result.overall_score >= 70
            else
            "Needs Improvement"
        ),

    )

    # ======================================================
    # Resume Summary
    # ======================================================

    render_summary_card(

        review.summary,

    )

    # ======================================================
    # Skills Overview
    # ======================================================

    render_skills_overview(

        ats_result.matched_skills,

        ats_result.missing_skills,

    )

    # ======================================================
    # Review Overview
    # ======================================================

    render_review_overview(

        review,

    )

    # ======================================================
    # Recommendation Overview
    # ======================================================

    render_recommendation_overview(

        recommendations,

    )

    # ======================================================
    # Export Report
    # ======================================================

    # render_export_report(
    #     candidate_name=getattr(
    #         resume_data,
    #         "name",
    #         "Unknown Candidate",
    #     ),
    #     ats_result=ats_result,
    #     review=review,
    #     recommendations=recommendations,
    #     interview=interview,
    #     cover_letter=cover_letter,
    # )
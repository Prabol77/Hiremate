"""
HireMate Overview Dashboard.

Responsibilities:
- Dashboard Header
- Hero Metrics
- Resume Analytics
- Recruiter Assessment
- AI Insights
- Resume Strength
"""

import streamlit as st

from components.ui.metric_card_v2 import (
    render_metric_card_v2,
)

from components.charts.ats_gauge import (
    render_ats_gauge,
)

from components.charts.skills_donut import (
    render_skills_donut,
)

from components.dashboard.ats_breakdown import (
    render_ats_breakdown,
)

from components.dashboard.recruiter_panel import (
    render_recruiter_panel,
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

from components.dashboard.resume_strength import (
    render_resume_strength,
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
    Render HireMate Overview Dashboard.
    """

    # =====================================================
    # Header
    # =====================================================

    st.title("🤖 HireMate Dashboard")

    st.caption(
        "AI-powered resume analysis and career insights."
    )

    st.divider()

    # =====================================================
    # Hero Metrics
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_metric_card_v2(
            icon="🎯",
            title="ATS Score",
            value=f"{ats_result.overall_score:.0f}%",
            subtitle="Resume Match",
        )

    with col2:

        render_metric_card_v2(
            icon="✅",
            title="Matched Skills",
            value=str(len(ats_result.matched_skills)),
            subtitle="Skills Found",
        )

    with col3:

        render_metric_card_v2(
            icon="⚠️",
            title="Missing Skills",
            value=str(len(ats_result.missing_skills)),
            subtitle="Need Improvement",
        )

    with col4:

        grade = (
            "A+"
            if ats_result.overall_score >= 85
            else "B+"
            if ats_result.overall_score >= 70
            else "C"
        )

        render_metric_card_v2(
            icon="⭐",
            title="Resume Grade",
            value=grade,
            subtitle="Overall Quality",
        )

    st.divider()

    # =====================================================
    # Resume Analytics
    # =====================================================

    st.subheader("📊 Resume Analytics")

    chart1, chart2 = st.columns(2)

    with chart1:

        render_ats_gauge(
            ats_result.overall_score,
        )

    with chart2:

        render_skills_donut(
            len(ats_result.matched_skills),
            len(ats_result.missing_skills),
        )

    st.divider()

    render_ats_breakdown(
        ats_result,
    )

    st.divider()

    # =====================================================
    # Recruiter Assessment
    # =====================================================

    render_recruiter_panel(
        resume_data,
        ats_result,
    )

    st.divider()

    # =====================================================
    # AI Summary & Skills
    # =====================================================

    left, right = st.columns(
        [2, 1],
        gap="large",
    )

    with left:

        render_summary_card(
            review.summary,
        )

    with right:

        render_skills_overview(
            ats_result.matched_skills,
            ats_result.missing_skills,
        )

    st.divider()

    # =====================================================
    # AI Review & Recommendations
    # =====================================================

    left, right = st.columns(
        [2, 1],
        gap="large",
    )

    with left:

        render_review_overview(
            review,
        )

    with right:

        render_recommendation_overview(
            recommendations,
        )

    st.divider()

    # =====================================================
    # Resume Strength
    # =====================================================

    render_resume_strength(
        resume_data,
        ats_result,
    )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption(
        "HireMate v0.6 • AI Resume Intelligence Dashboard"
    )
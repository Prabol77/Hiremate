"""
Overview Dashboard Tab.

Responsibilities:
- Resume statistics
- ATS score
- Summary metrics
- Charts
- PDF export
"""

from components.cards.ats_card import (
    render_ats_card,
)

from components.cards.statistics_card import (
    render_statistics_card,
)

from components.cards.summary_card import (
    render_summary_card,
)

from components.charts.gauge_chart import (
    render_gauge,
)

from components.charts.skill_chart import (
    render_skill_chart,
)

from components.export_button import (
    render_export_button,
)

import streamlit as st


# ==========================================================
# Overview Tab
# ==========================================================


def render_overview_tab(
    resume_pdf,
    resume_data,
    ats_result,
    review,
    recommendations,
    interview,
):
    """
    Render the Overview dashboard tab.
    """

    left, right = st.columns(2)

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    with left:

        render_statistics_card(
            resume_pdf,
        )

    # ------------------------------------------------------
    # ATS Score
    # ------------------------------------------------------

    with right:

        render_ats_card(
            ats_result.overall_score,
        )

    st.divider()

    # ------------------------------------------------------
    # Summary
    # ------------------------------------------------------

    render_summary_card(
        ats_result,
    )

    st.divider()

    # ------------------------------------------------------
    # Charts
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # Export
    # ------------------------------------------------------

    render_export_button(
        resume_data,
        ats_result,
        review,
        recommendations,
        interview,
    )
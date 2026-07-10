"""
Skill Gap Dashboard Panel.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def _render_group(
    title,
    color,
    skills,
):

    st.subheader(
        f"{color} {title} ({len(skills)})"
    )

    if not skills:

        st.success(
            "No skills."
        )

        return

    for gap in skills:

        with st.container(
            border=True,
        ):

            st.markdown(
                f"### {gap.skill}"
            )

            st.caption(
                gap.reason
            )


def render_skill_gap_panel(
    gap_result,
):
    """
    Render Skill Gap Dashboard.
    """

    render_section_header(

        "🎯 Skill Gap Analysis",

        "Prioritized skills required to improve your ATS score.",

    )

    st.metric(

        "Overall Skill Match",

        f"{gap_result.overall_score}%",

    )

    st.progress(
        gap_result.overall_score / 100,
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        _render_group(

            "High Priority",

            "🔴",

            gap_result.high_priority,

        )

        st.divider()

        _render_group(

            "Medium Priority",

            "🟡",

            gap_result.medium_priority,

        )

    with right:

        _render_group(

            "Low Priority",

            "🟢",

            gap_result.low_priority,

        )
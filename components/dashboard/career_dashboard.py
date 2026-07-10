"""
Career Development Dashboard.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)
from components.dashboard.career_summary import (
    render_career_summary,
)

def _render_priority_skills(
    skill_gap,
):

    st.subheader("🎯 Priority Skills")

    if skill_gap.high_priority:

        for gap in skill_gap.high_priority:

            st.error(gap.skill)

    elif skill_gap.medium_priority:

        for gap in skill_gap.medium_priority:

            st.warning(gap.skill)

    else:

        st.success(
            "No major skill gaps detected."
        )


def _render_next_tasks(
    roadmap,
):

    st.subheader("🗺 Next Learning Tasks")

    if not roadmap.tasks:

        st.info(
            "No roadmap available."
        )

        return

    for task in roadmap.tasks[:5]:

        with st.container(
            border=True,
        ):

            st.markdown(
                f"### Week {task.week}"
            )

            st.write(task.title)

            st.caption(
                task.description
            )


def render_career_dashboard(
    skill_gap,
    roadmap,
):
    """
    Unified Career Dashboard.
    """

    render_section_header(

        "🚀 Career Development",

        "Personalized learning and career growth plan.",

    )

    render_career_summary(
            skill_gap,
            roadmap,
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "Career Readiness",

            f"{skill_gap.overall_score}%",

        )

    with col2:

        st.metric(

            "Learning Duration",

            f"{roadmap.duration_weeks} Weeks",

        )

    st.progress(
        skill_gap.overall_score / 100,
    )

    st.divider()

    left, right = st.columns(
        [1, 2],
        gap="large",
    )

    with left:

        _render_priority_skills(
            skill_gap,
        )

    with right:

        _render_next_tasks(
            roadmap,
        )
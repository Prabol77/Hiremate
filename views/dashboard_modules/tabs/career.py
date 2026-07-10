"""
Career Workspace.

Combines:
- Career Intelligence
- Skill Gap
- Learning Roadmap
"""

import streamlit as st

from components.dashboard.career_summary import (
    render_career_summary,
)

from views.dashboard_modules.tabs.skill_gap import (
    render_skill_gap_tab,
)

from views.dashboard_modules.tabs.roadmap import (
    render_roadmap_tab,
)


def render_career_tab(
    career,
    skill_gap,
    roadmap,
):
    """
    Render Career workspace.
    """

    st.title("🚀 Career Development")

    # ======================================================
    # Career Intelligence
    # ======================================================

    render_career_summary(
        career,
    )

    st.divider()

    # ======================================================
    # Skill Gap
    # ======================================================

    render_skill_gap_tab(
        skill_gap,
    )

    st.divider()

    # ======================================================
    # Learning Roadmap
    # ======================================================

    render_roadmap_tab(
        roadmap,
    )
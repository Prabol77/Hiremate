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
from components.dashboard.personalization_card import (
    render_personalization_card,
)
from components.dashboard.hireability_card import (
    render_hireability_card,
)

from components.dashboard.career_coach_card import (
    render_career_coach_card,
)

from components.dashboard.project_recommendations import (
    render_project_recommendations,
)

from components.dashboard.career_summary import (
    render_career_summary,
)

from components.dashboard.career_coach_card import (
    render_career_coach_card,
)

from components.dashboard.project_recommendations import (
    render_project_recommendations,
)

from views.dashboard_modules.tabs.skill_gap import (
    render_skill_gap_tab,
)

from views.dashboard_modules.tabs.roadmap import (
    render_roadmap_tab,
)

from components.dashboard.company_match_card import (
    render_company_match_card,
)

from components.dashboard.certification_card import (
    render_certification_card,
)

def render_career_tab(
    career,
    hireability,
    career_coach,
    projects,
    company_matches,
    certifications,
    personalization,
    skill_gap,
    roadmap,
):
    """
    Render Career workspace.
    """
    # ======================================================
    # Career Intelligence
    # ======================================================
    st.title(
        "🚀 Career Development"
    )

    render_career_coach_card(
        career_coach,
    )

    st.divider()

    render_personalization_card(
        personalization,
    )

    st.divider()

    render_hireability_card(
        hireability,
    )

    st.divider()

    render_career_summary(
        career,
    )

    st.divider()

    render_project_recommendations(
        projects,
    )

    st.divider()

    render_company_match_card(
        company_matches,
    )

    st.divider()

    render_certification_card(
        certifications,
    )

    st.divider()

    render_skill_gap_tab(
        skill_gap,
    )

    st.divider()

    render_roadmap_tab(
        roadmap,
    )
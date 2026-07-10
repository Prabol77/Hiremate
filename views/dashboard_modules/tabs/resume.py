"""
Resume Workspace.

Combines:
- Candidate Profile
- Skills
- Resume Review
"""

import streamlit as st

from views.dashboard_modules.tabs.candidate import (
    render_candidate_tab,
)

from views.dashboard_modules.tabs.skills import (
    render_skills_tab,
)

from views.dashboard_modules.tabs.review import (
    render_review_tab,
)


def render_resume_tab(
    resume_data,
    resume_text,
    ats_result,
    review,
):
    """
    Render the Resume workspace.
    """

    st.subheader("👤 Resume Workspace")

    render_candidate_tab(
        resume_data,
        resume_text,
    )

    st.divider()

    render_skills_tab(
        ats_result,
    )

    st.divider()

    render_review_tab(
        review,
    )
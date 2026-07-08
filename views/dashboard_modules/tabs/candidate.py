"""
Candidate Tab.
"""

from components.dashboard.candidate_profile import (
    render_candidate_profile,
)


def render_candidate_tab(
    resume_data,
    resume_text,
):
    """
    Render candidate profile.
    """

    render_candidate_profile(
        resume_data,
    )
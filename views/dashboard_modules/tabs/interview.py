"""
Interview Dashboard Tab.

Responsibilities:
- Display AI-generated interview questions
- Display interview preparation tips
"""

import streamlit as st

from models.interview_model import InterviewResult

from components.cards.interview_card import (
    render_interview_card,
)


# ==========================================================
# Interview Tab
# ==========================================================


def render_interview_tab(
    interview: InterviewResult,
):
    """
    Render the AI Interview Preparation dashboard tab.
    """

    render_interview_card(
        interview,
    )

    st.divider()

    total_questions = sum(
        len(questions)
        for questions in interview.questions.values()
    )

    if total_questions > 0:

        st.success(
            f"{total_questions} interview question(s) generated."
        )

    else:

        st.warning(
            "No interview questions were generated."
        )

    if interview.overall_tips:

        st.info(
            f"{len(interview.overall_tips)} interview preparation tip(s) available."
        )

    st.caption(
        "Interview questions are generated using your resume "
        "and the uploaded job description to simulate a realistic "
        "technical interview."
    )
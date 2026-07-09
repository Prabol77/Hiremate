"""
Interview Questions.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def render_interview_details(interview):

    render_section_header(
        "🎤 Interview Preparation",
        "Personalized interview questions.",
    )

    if not interview.questions:

        st.info("No interview questions generated.")

        return

    for category, questions in interview.questions.items():

        st.subheader(category)

        for question in questions:

            st.markdown(f"• {question}")

        st.divider()

    if interview.overall_tips:

        st.subheader("💡 Overall Tips")

        for tip in interview.overall_tips:

            st.info(tip)
"""
Dashboard Interview Details.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)

from components.ui.status_badge import (
    render_status_badge,
)


# ==========================================================
# Helpers
# ==========================================================

def _render_question_group(
    title: str,
    questions: list[str],
):
    """
    Render one interview question category.
    """

    st.subheader(title)

    if questions:

        for index, question in enumerate(
            questions,
            start=1,
        ):

            st.markdown(
                f"**{index}.** {question}"
            )

    else:

        render_status_badge(
            "info",
            "No questions generated.",
        )

    st.divider()


# ==========================================================
# Main Renderer
# ==========================================================

def render_interview_details(
    interview,
):
    """
    Render interview preparation section.
    """

    render_section_header(
        "🎤 Interview Preparation",
        "Practice AI-generated interview questions tailored to your resume and job description.",
    )

    questions = getattr(
        interview,
        "questions",
        {},
    ) or {}

    if not questions:

        render_status_badge(
            "warning",
            "No interview questions available.",
        )

        return

    # Automatically render every category
    for category, question_list in questions.items():

        icon = {
            "Technical": "💻",
            "Programming": "⌨️",
            "Projects": "🚀",
            "Behavioral": "🧠",
            "HR": "🤝",
        }.get(category, "📌")

        _render_question_group(
            f"{icon} {category} Questions",
            question_list,
        )

    # ======================================================
    # Interview Tips
    # ======================================================

    tips = getattr(
        interview,
        "overall_tips",
        [],
    )

    if tips:

        st.subheader("💡 Interview Tips")

        for tip in tips:

            render_status_badge(
                "success",
                tip,
            )
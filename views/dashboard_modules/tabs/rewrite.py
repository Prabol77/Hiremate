"""
Rewrite Dashboard Tab.

Responsibilities:
- Preview resume sections
- Rewrite individual sections using AI
- Display rewritten content
"""

import streamlit as st

from models.resume_model import ResumeData

from services.ai_service import AIService

from components.cards.rewrite_card import (
    render_rewrite_card,
)


# ==========================================================
# Rewrite Tab
# ==========================================================


def render_rewrite_tab(
    resume_data: ResumeData,
    jd_text: str,
):
    """
    Render the AI Resume Rewrite dashboard tab.
    """

    st.header("✨ AI Resume Rewrite")

    st.write(
        "Select a resume section to improve. "
        "HireMate rewrites your content while preserving factual accuracy."
    )

    if not resume_data.sections:

        st.info(
            "No resume sections were detected."
        )

        return

    ai_service = AIService()

    # ------------------------------------------------------
    # Resume Sections
    # ------------------------------------------------------

    for section_name, section_text in resume_data.sections.items():

        if not section_text.strip():

            continue

        with st.expander(
            f"📄 {section_name.title()}",
            expanded=False,
        ):

            st.text_area(
                label="Current Content",
                value=section_text,
                height=180,
                disabled=True,
                key=f"{section_name}_preview",
            )

            if st.button(
                f"✨ Rewrite {section_name.title()}",
                key=f"rewrite_{section_name}",
                use_container_width=True,
            ):

                with st.spinner(
                    "Generating improved version..."
                ):

                    rewrite = ai_service.rewrite_resume(
                        section_name=section_name,
                        section_text=section_text,
                        jd_text=jd_text,
                    )

                st.divider()

                render_rewrite_card(
                    rewrite,
                )

    st.divider()

    st.caption(
        "HireMate improves wording, grammar, ATS keywords and "
        "professional tone without inventing new experience."
    )
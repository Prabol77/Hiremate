import streamlit as st

from services.ai_service import AIService

from components.cards.cover_letter_card import (
    render_cover_letter_card,
)


@st.cache_resource
def get_ai_service():
    """
    Return a cached AI service instance.
    """

    return AIService()


# ==========================================================
# Cover Letter Tab
# ==========================================================


def render_cover_letter_tab(
    resume_text: str,
    jd_text: str,
):
    """
    Render the AI Cover Letter dashboard tab.
    """

    st.header("📄 AI Cover Letter Generator")

    st.write(
        """
Generate a personalized, ATS-friendly cover letter
tailored to the uploaded resume and job description.
"""
    )

    # ------------------------------------------------------
    # Style Selection
    # ------------------------------------------------------

    style = st.radio(
        "Choose Cover Letter Style",
        (
            "Professional",
            "Modern",
            "Concise",
        ),
        horizontal=True,
    )

    st.divider()

    ai_service = get_ai_service()

    # ------------------------------------------------------
    # Generate
    # ------------------------------------------------------

    generate = st.button(
        "🚀 Generate Cover Letter",
        use_container_width=True,
    )

    if generate:

        with st.spinner(
            "Generating cover letter..."
        ):

            result = ai_service.generate_cover_letter(
                resume_text,
                jd_text,
                style,
            )

        st.session_state["cover_letter"] = result

    # ------------------------------------------------------
    # Regenerate
    # ------------------------------------------------------

    if "cover_letter" in st.session_state:

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔄 Regenerate",
                use_container_width=True,
            ):

                with st.spinner(
                    "Generating another version..."
                ):

                    st.session_state["cover_letter"] = (
                        ai_service.generate_cover_letter(
                            resume_text,
                            jd_text,
                            style,
                        )
                    )

        with col2:

            st.success(
                "Cover letter ready."
            )

        st.divider()

        render_cover_letter_card(
            st.session_state["cover_letter"]
        )
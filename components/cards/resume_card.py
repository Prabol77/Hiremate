import streamlit as st

from models.resume_model import ResumeData


def render_resume_card(
    resume: ResumeData,
) -> None:
    """
    Render candidate information.

    Args:
        resume:
            Parsed resume data.
    """

    st.header("👤 Candidate Information")

    info = resume.personal_info

    left_fields = [
        (
            "Name",
            info.name,
        ),
        (
            "Email",
            info.email,
        ),
        (
            "Phone",
            info.phone,
        ),
    ]

    right_fields = [
        (
            "Location",
            info.location,
        ),
        (
            "LinkedIn",
            info.linkedin,
        ),
        (
            "GitHub",
            info.github,
        ),
    ]

    col1, col2 = st.columns(2)

    with col1:

        for label, value in left_fields:

            st.write(f"**{label}:** {value or 'Not Available'}")

    with col2:

        for label, value in right_fields:

            st.write(f"**{label}:** {value or 'Not Available'}")

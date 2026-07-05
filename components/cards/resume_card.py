import streamlit as st

from models.resume_model import ResumeData


def render_resume_card(
    resume: ResumeData,
):
    """
    Render candidate information.
    """

    st.header("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Name:** {resume.personal_info.name}"
        )

        st.write(
            f"**Email:** {resume.personal_info.email}"
        )

        st.write(
            f"**Phone:** {resume.personal_info.phone}"
        )

    with col2:

        st.write(
            f"**Location:** {resume.personal_info.location}"
        )

        st.write(
            f"**LinkedIn:** {resume.personal_info.linkedin}"
        )

        st.write(
            f"**GitHub:** {resume.personal_info.github}"
        )
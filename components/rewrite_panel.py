import streamlit as st

from models.resume_model import ResumeData
from models.rewrite_model import RewriteResult


def render_rewrite_panel(
    resume: ResumeData,
):
    """
    Render the Resume Rewrite panel.
    """

    st.subheader("✨ AI Resume Rewrite")

    if not resume.sections:

        st.warning("No resume sections were detected.")

        return None

    section = st.selectbox(
        "Choose a resume section",
        options=list(resume.sections.keys()),
        index=0,
    )

    st.caption("Only the selected section will be rewritten.")

    rewrite_clicked = st.button(
        "✨ Rewrite Section",
        use_container_width=True,
    )

    if not rewrite_clicked:

        return None

    return {
        "section_name": section,
        "section_text": resume.sections[section],
    }

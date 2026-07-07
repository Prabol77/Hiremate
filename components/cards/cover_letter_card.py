import streamlit as st

from models.cover_letter_model import CoverLetterResult


def render_cover_letter_card(
    cover_letter: CoverLetterResult,
):
    """
    Render the AI-generated cover letter.
    """

    st.header("📄 AI Cover Letter")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Company",
            cover_letter.company_name or "Unknown",
        )

    with col2:

        st.metric(
            "Position",
            cover_letter.position or "Unknown",
        )

    st.divider()

    sections = [
        cover_letter.greeting,
        cover_letter.introduction,
        cover_letter.body,
        cover_letter.conclusion,
        cover_letter.closing,
    ]

    content = "\n\n".join(
        section.strip()
        for section in sections
        if section.strip()
    )

    if not content:

        content = cover_letter.full_letter

    st.text_area(
        label="Generated Cover Letter",
        value=content,
        height=450,
        disabled=True,
    )

    st.download_button(
        label="⬇ Download Cover Letter (.txt)",
        data=content,
        file_name="Cover_Letter.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.caption(
        "Review the generated cover letter before submitting "
        "it with your application."
    )
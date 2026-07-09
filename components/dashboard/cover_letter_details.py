"""
Cover Letter Details.
"""

import streamlit as st

from components.ui.section_header import (
    render_section_header,
)


def render_cover_letter_details(
    cover_letter,
):

    render_section_header(
        "📄 AI Cover Letter",
        "Generated cover letter.",
    )

    st.markdown(
        cover_letter.full_letter,
    )
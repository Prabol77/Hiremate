import streamlit as st

from config import MAX_PREVIEW_CHARS


def render_preview_card(text):
    """
    Resume Preview.
    """

    with st.expander("📄 Resume Preview"):

        st.text_area(
            "",
            value=text[:MAX_PREVIEW_CHARS],
            height=350,
        )

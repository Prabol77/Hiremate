from pathlib import Path

import streamlit as st


def load_theme():
    """
    Load the HireMate design system.
    """

    css_path = Path("styles/style.css")

    if css_path.exists():

        css = css_path.read_text(
            encoding="utf-8"
        )

        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True,
        )
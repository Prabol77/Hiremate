"""
Reusable dashboard section header.
"""

import streamlit as st


def render_section_header(
    title: str,
    description: str | None = None,
):
    """
    Render a standard HireMate section header.
    """

    st.title(title)

    if description:

        st.caption(description)

    st.divider()
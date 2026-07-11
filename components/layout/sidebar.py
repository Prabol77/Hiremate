"""
HireMate Sidebar.
"""

import streamlit as st


def render_sidebar() -> str:
    """
    Render the application sidebar.

    Returns
    -------
    str
        Selected page.
    """

    with st.sidebar:

        st.title("💼 HireMate")

        st.caption(
            "Version 0.8.0"
        )

        st.divider()

        page = st.radio(
            "Navigation",
            (
                "🏠 Dashboard",
                "📘 Product Info",
            ),
        )

    return page
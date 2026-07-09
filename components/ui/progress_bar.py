"""
Reusable Progress Bar.
"""

import streamlit as st


def render_progress_bar(
    title: str,
    value: float,
):
    """
    Render a labeled progress bar.
    """

    st.write(f"**{title}**")

    st.progress(
        value / 100,
    )

    st.caption(
        f"{value:.0f}%"
    )
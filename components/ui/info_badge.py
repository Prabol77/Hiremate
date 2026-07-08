"""
Reusable information badge.
"""

import streamlit as st


def render_info_badge(
    label: str,
    value: str,
):
    """
    Render an information badge.

    Args:
        label:
            Badge label.

        value:
            Badge value.
    """

    st.markdown(f"##### {label}")

    st.info(
        value if value else "Not Available"
    )
"""
Reusable document preview component.
"""

import streamlit as st


def render_document_preview(
    title: str,
    content: str,
    *,
    height: int = 350,
):
    """
    Render a document preview.
    """

    st.subheader(title)

    widget_key = (
        "preview_"
        + title.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )

    st.text_area(
        label=title,
        value=content or "",
        height=height,
        disabled=True,
        key=widget_key,
    )
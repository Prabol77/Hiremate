"""
Resume Preview Card.

Displays a preview of the extracted resume text.
"""

import streamlit as st


# ==========================================================
# Resume Preview Card
# ==========================================================


def render_preview_card(
    text: str,
):
    """
    Render a preview of the extracted resume text.

    Args:
        text (str):
            Extracted resume text.
    """

    st.subheader("📄 Resume Preview")

    with st.expander(
        "View Extracted Resume",
        expanded=False,
    ):

        st.text_area(
            label="Resume Content",
            value=text[:3000],
            height=350,
            disabled=True,
        )

        if len(text) > 3000:

            st.caption(
                "Only the first 3,000 characters are displayed."
            )
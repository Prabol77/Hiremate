import streamlit as st

MAX_PREVIEW_LENGTH = 3000


def render_preview_card(
    text: str,
) -> None:
    """
    Render a read-only preview of the extracted resume text.

    Args:
        text:
            Extracted resume text.
    """

    with st.expander(
        "📄 Resume Preview",
        expanded=False,
    ):

        if not text:

            st.info("No resume preview available.")

            return

        preview = text[:MAX_PREVIEW_LENGTH]

        st.text_area(
            label="Resume Content",
            value=preview,
            height=350,
            disabled=True,
        )

        if len(text) > MAX_PREVIEW_LENGTH:

            st.caption(
                f"Showing the first {MAX_PREVIEW_LENGTH:,} characters of the extracted resume."
            )

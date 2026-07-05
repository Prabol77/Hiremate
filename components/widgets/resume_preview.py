import streamlit as st


def render_preview_card(text: str):
    """
    Render resume preview widget.
    """

    with st.expander(
        "📄 Resume Preview",
        expanded=False,
    ):

        st.text_area(
            label="",
            value=text[:3000],
            height=350,
        )
import streamlit as st


def render_preview(text: str):
    """
    Resume preview.
    """

    with st.expander(
        "📄 Resume Preview",
        expanded=False,
    ):

        st.text_area(
            "",
            value=text[:3000],
            height=350,
        )
import streamlit as st


def render_section(
    title: str,
    description: str = "",
):
    """
    Render a section heading.
    """

    st.markdown(f"## {title}")

    if description:

        st.caption(description)

    st.divider()
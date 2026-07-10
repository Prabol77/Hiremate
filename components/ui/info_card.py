import streamlit as st


def render_info_card(
    title: str,
    value: str,
):
    with st.container(border=True):

        st.caption(title)

        st.markdown(
            f"## {value}"
        )
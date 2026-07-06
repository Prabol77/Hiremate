import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.

    Returns
    -------
    str
        Selected page.
    """

    with st.sidebar:

        st.title("💼 HireMate")

        st.markdown("---")

        page = st.radio(
            "Navigation",
            (
                "Dashboard",
                "Resume Analysis",
                "Interview Prep",
                "About",
            ),
        )

    return page

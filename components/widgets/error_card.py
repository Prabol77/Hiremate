import streamlit as st


def render_error_card(
    error: Exception,
) -> None:
    """
    Render a user-friendly error message.

    Args:
        error:
            Exception raised during analysis.
    """

    st.error("❌ Unable to complete the analysis.")

    st.info("Please verify that your uploaded files are valid and try again.")

    with st.expander(
        "🔍 Technical Details",
        expanded=False,
    ):

        st.exception(error)

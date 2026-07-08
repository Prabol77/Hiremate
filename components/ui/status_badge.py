"""
Reusable status badge.
"""

import streamlit as st


def render_status_badge(
    status: str,
    message: str,
):
    """
    Render a status message.

    Status values:
        success
        warning
        error
        info
    """

    status = status.lower()

    if status == "success":

        st.success(message)

    elif status == "warning":

        st.warning(message)

    elif status == "error":

        st.error(message)

    else:

        st.info(message)
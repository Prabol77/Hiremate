"""
Reusable Dashboard Card.
"""

from contextlib import contextmanager

import streamlit as st


@contextmanager
def dashboard_card(
    title: str,
    icon: str = "📊",
):
    """
    Render a reusable dashboard card.
    """

    with st.container(
        border=True,
    ):

        st.subheader(
            f"{icon} {title}"
        )

        yield
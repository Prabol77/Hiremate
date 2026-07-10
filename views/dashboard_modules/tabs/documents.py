"""
Documents Workspace.
"""

import streamlit as st

from views.dashboard_modules.tabs.cover_letter import (
    render_cover_letter_tab,
)


def render_documents_tab(
    cover_letter,
):
    """
    Render Documents workspace.
    """

    st.subheader("📄 Documents")

    render_cover_letter_tab(
        cover_letter,
    )
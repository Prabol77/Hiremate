"""
Reusable Status Badge.
"""

import streamlit as st


def render_status_badge(
    label: str,
    priority: str,
):
    """
    Render a consistent priority badge.
    """

    badges = {
        "High": "🔥 High Priority",
        "Medium": "⚡ Medium Priority",
        "Low": "💡 Low Priority",
        "Completed": "✅ Completed",
    }

    badge = badges.get(
        priority,
        "ℹ️ Info",
    )

    st.caption(
        f"{badge} • {label}"
    )
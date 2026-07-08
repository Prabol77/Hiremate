"""
Reusable metric card for HireMate.
"""

import streamlit as st


def render_metric_card(
    title: str,
    value,
    delta: str | None = None,
    help_text: str | None = None,
):
    """
    Render a standardized metric card.

    Args:
        title:
            Metric title.

        value:
            Metric value.

        delta:
            Optional delta text.

        help_text:
            Tooltip shown on hover.
    """

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text,
    )
import streamlit as st

from models.ats_model import ATSResult


def render_summary_card(
    result: ATSResult,
) -> None:
    """
    Render a summary of the ATS analysis.

    Args:
        result:
            ATS analysis result.
    """

    statistics = [
        (
            "Matched",
            len(result.matched_skills or []),
        ),
        (
            "Missing",
            len(result.missing_skills or []),
        ),
        (
            "Additional",
            len(result.additional_skills or []),
        ),
    ]

    columns = st.columns(len(statistics))

    for column, (label, value) in zip(
        columns,
        statistics,
    ):
        column.metric(
            label,
            value,
        )

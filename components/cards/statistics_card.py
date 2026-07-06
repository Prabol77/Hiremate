import streamlit as st


def render_statistics_card(
    pdf_data: dict,
) -> None:
    """
    Render document statistics.

    Args:
        pdf_data:
            Dictionary containing PDF metadata.
    """

    st.subheader("📊 Document Statistics")

    statistics = [
        (
            "Pages",
            pdf_data.get("pages", 0),
        ),
        (
            "Words",
            pdf_data.get("words", 0),
        ),
        (
            "Characters",
            pdf_data.get("characters", 0),
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

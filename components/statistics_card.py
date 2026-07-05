import streamlit as st


def render_statistics(pdf_data: dict):
    """
    Display document statistics.
    """

    st.subheader("📊 Document Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Pages",
        pdf_data["pages"],
    )

    col2.metric(
        "Words",
        pdf_data["words"],
    )

    col3.metric(
        "Characters",
        pdf_data["characters"],
    )
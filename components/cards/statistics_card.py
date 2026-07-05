import streamlit as st


def render_statistics_card(pdf_data):
    """
    Render PDF statistics.
    """

    st.subheader("📊 Document Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Pages",
        pdf_data["pages"]
    )

    c2.metric(
        "Words",
        pdf_data["words"]
    )

    c3.metric(
        "Characters",
        pdf_data["characters"]
    )
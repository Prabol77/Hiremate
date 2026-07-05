import streamlit as st


def render_ats_score(score: float):
    """
    Display ATS score.
    """

    st.header("🎯 ATS Match Score")

    st.metric(
        "Overall Match",
        f"{score:.2f}%"
    )

    st.progress(score / 100)
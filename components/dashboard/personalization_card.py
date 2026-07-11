"""
AI Personalization Dashboard.
"""

import streamlit as st


# ==========================================================
# AI Personalized Insights
# ==========================================================


def render_personalization_card(
    personalization,
):
    """
    Render AI personalized career insights.
    """

    st.subheader(
        "✨ Personalized AI Insights"
    )

    # ======================================================
    # Career Summary
    # ======================================================

    st.info(
        personalization.career_summary,
    )

    st.divider()

    # ======================================================
    # Why These Projects?
    # ======================================================

    st.markdown(
        "### 🚀 Why These Projects?"
    )

    st.write(
        personalization.why_projects,
    )

    st.divider()

    # ======================================================
    # Why These Certifications?
    # ======================================================

    st.markdown(
        "### 📜 Why These Certifications?"
    )

    st.write(
        personalization.why_certifications,
    )

    st.divider()

    # ======================================================
    # Why These Companies?
    # ======================================================

    st.markdown(
        "### 🏢 Why These Companies?"
    )

    st.write(
        personalization.why_companies,
    )

    st.divider()

    # ======================================================
    # Final Advice
    # ======================================================

    st.success(
        personalization.final_advice,
    )
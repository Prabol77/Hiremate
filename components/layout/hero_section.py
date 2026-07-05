import streamlit as st


def render_hero_section():
    """
    Render the landing hero section.
    """

    st.title("💼 HireMate")

    st.subheader(
        "AI-Powered Resume Intelligence Platform"
    )

    st.write(
        """
Analyze your resume against a job description to discover
your ATS score, identify missing skills, and prepare for
technical interviews with AI-powered insights.
"""
    )

    st.markdown("### What HireMate Offers")

    feature_col1, feature_col2 = st.columns(2)

    with feature_col1:

        st.success("✔ ATS Resume Matching")

        st.success("✔ Skill Gap Analysis")

        st.success("✔ Resume Intelligence")

    with feature_col2:

        st.success("✔ AI Career Coach (Coming Soon)")

        st.success("✔ Interview Preparation")

        st.success("✔ Learning Roadmap")

    st.divider()
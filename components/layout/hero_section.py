import streamlit as st


def render_hero_section() -> None:
    """
    Render the HireMate landing hero section.
    """

    st.title("💼 HireMate")
    st.caption("Version 0.8.0 • AI Career Intelligence Platform")

    st.subheader(
        "AI-Powered Career Intelligence Platform"
    )

    st.write(
        """
Analyze your resume against a job description to evaluate ATS compatibility,
identify skill gaps, improve hireability, receive AI-powered career coaching,
discover company matches, earn certification recommendations, and prepare
for interviews.
"""
    )

    st.divider()

    st.markdown("### ✨ What HireMate Offers")

    features_left = [

        "🎯 ATS Resume Matching",

        "🧠 AI Career Coach",

        "🏆 Hireability Intelligence",

        "🏢 Company Match Intelligence",

    ]

    features_right = [

        "🛠 Skill Gap Analysis",

        "📜 Certification Intelligence",

        "🎤 Interview Preparation",

        "🗺 Personalized Learning Roadmap",

    ]

    col1, col2 = st.columns(2)

    with col1:

        for feature in features_left:

            st.success(feature)

    with col2:

        for feature in features_right:

            st.success(feature)

    st.divider()
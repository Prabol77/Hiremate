import streamlit as st


def render_hero_section() -> None:
    """
    Render the HireMate landing hero section.
    """

    st.title("💼 HireMate")

    st.subheader("AI-Powered Resume Intelligence Platform")

    st.write("""
Analyze your resume against a job description to evaluate
ATS compatibility, identify missing skills, receive
AI-powered resume feedback, and prepare for interviews.
""")

    st.divider()

    st.markdown("### ✨ What HireMate Offers")

    available_features = [
        "🎯 ATS Resume Matching",
        "🛠 Skill Gap Analysis",
        "🤖 AI Resume Intelligence",
    ]

    upcoming_features = [
        "🚧 AI Career Coach (Coming Soon)",
        "🎤 Interview Preparation",
        "📚 Learning Roadmap",
    ]

    col1, col2 = st.columns(2)

    with col1:

        for feature in available_features:

            st.success(feature)

    with col2:

        for feature in upcoming_features:

            if "Coming Soon" in feature:

                st.info(feature)

            else:

                st.success(feature)

    st.divider()

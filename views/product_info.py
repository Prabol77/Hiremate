"""
HireMate Product Information.
"""

import streamlit as st


def show_product_info():
    """
    Render the HireMate product information page.
    """

    st.title("💼 HireMate")

    st.caption(
        "Version 0.8.0"
    )

    st.subheader(
        "AI-Powered Career Intelligence Platform"
    )

    st.write(
        """
HireMate is an AI-powered platform that analyzes resumes,
evaluates ATS compatibility, identifies skill gaps,
recommends projects and certifications, matches candidates
with companies, and provides personalized career guidance.
"""
    )

    st.divider()

    # ======================================================
    # Features
    # ======================================================

    st.header("✨ Key Features")

    features = [

        "🎯 ATS Resume Matching",

        "🧠 AI Career Coach",

        "🏆 Hireability Intelligence",

        "🏢 Company Match Intelligence",

        "📜 Certification Intelligence",

        "🚀 Project Recommendations",

        "🛠 Skill Gap Analysis",

        "🗺 Personalized Learning Roadmap",

        "🎤 Interview Preparation",

        "📄 AI Cover Letter Generation",

    ]

    for feature in features:

        st.success(
            feature,
        )

    st.divider()

    # ======================================================
    # Technology Stack
    # ======================================================

    st.header("🛠 Technology Stack")

    st.markdown(
        """
- Python
- Streamlit
- Groq API
- OCR & Resume Parsing
- Custom ATS Engine
- Modular Service Architecture
"""
    )

    st.divider()

    # ======================================================
    # Roadmap
    # ======================================================

    st.header("🗺 Roadmap")

    roadmap = {

        "✅ v0.8.0": "Career Intelligence Platform",

        "🔜 v0.9.0": "Authentication & Progress Tracking",

        "🚀 v1.0.0": "Production Release",

    }

    for version, description in roadmap.items():

        st.write(
            f"**{version}** — {description}"
        )

    st.divider()

    # ======================================================
    # Footer
    # ======================================================

    st.caption(
        "Built with ❤️ using Streamlit & AI."
    )
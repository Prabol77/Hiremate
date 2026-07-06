import streamlit as st


def render_empty_state() -> None:
    """
    Render the dashboard empty state shown before
    any files are uploaded.
    """

    st.title("🚀 Welcome to HireMate")

    st.write(
        "Analyze your resume against any job description " "using AI-powered insights."
    )

    st.divider()

    st.subheader("✨ What You'll Get")

    features = [
        "🎯 ATS Match Score",
        "🛠 Skill Gap Analysis",
        "🤖 AI Resume Review",
        "📈 AI Career Recommendations",
        "🎤 AI Interview Questions",
        "📄 Professional PDF Report",
    ]

    for feature in features:
        st.markdown(f"- {feature}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Resume")

        st.markdown("- PDF")

    with col2:

        st.subheader("💼 Job Description")

        st.markdown("- PDF")
        st.markdown("- TXT")

    st.info("Upload both your Resume and Job Description to begin the analysis.")

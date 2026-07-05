import streamlit as st

from config import (
    MAX_PREVIEW_CHARS,
    SUPPORTED_JD_TYPES,
    SUPPORTED_RESUME_TYPES,
)

from components.uploader import save_uploaded_file

from utils.parser import extract_pdf_data

from services.analysis_service import AnalysisService


def show_dashboard():
    """
    Render HireMate Dashboard.
    """

    st.title("💼 HireMate")
    st.subheader("AI-Powered Resume & Job Matching Assistant")

    st.write(
        "Upload a Resume and a Job Description to evaluate compatibility."
    )

    st.divider()

    # =====================================================
    # File Upload Section
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📄 Resume")

        resume = st.file_uploader(
            "Upload Resume",
            type=SUPPORTED_RESUME_TYPES,
            key="resume",
        )

    with col2:

        st.markdown("### 💼 Job Description")

        jd = st.file_uploader(
            "Upload Job Description",
            type=SUPPORTED_JD_TYPES,
            key="jd",
        )

    # =====================================================
    # Wait until both files are uploaded
    # =====================================================

    if not (resume and jd):

        st.info(
            "Upload both Resume and Job Description to begin analysis."
        )

        return

    # =====================================================
    # Analysis
    # =====================================================

    try:

        # ---------------------------------------------
        # Save uploaded files
        # ---------------------------------------------

        resume_path = save_uploaded_file(resume)
        jd_path = save_uploaded_file(jd)

        # ---------------------------------------------
        # Resume Parsing
        # ---------------------------------------------

        resume_pdf = extract_pdf_data(resume_path)

        resume_text = resume_pdf["text"]

        # ---------------------------------------------
        # Job Description Parsing
        # ---------------------------------------------

        if jd.name.lower().endswith(".pdf"):

            jd_pdf = extract_pdf_data(jd_path)

            jd_text = jd_pdf["text"]

        else:

            with open(
                jd_path,
                "r",
                encoding="utf-8",
            ) as file:

                jd_text = file.read()

        # ---------------------------------------------
        # Run Complete Analysis
        # ---------------------------------------------

        analysis_service = AnalysisService()

        resume_data, job_data, ats_result = (
            analysis_service.analyze(
                resume_text,
                jd_text,
            )
        )

        st.success("✅ Analysis completed successfully!")

        st.divider()

        # =====================================================
        # ATS SCORE
        # =====================================================

        st.header("🎯 ATS Match Score")

        st.metric(
            "Overall Match",
            f"{ats_result.overall_score:.2f}%",
        )

        st.progress(
            ats_result.overall_score / 100
        )

        st.divider()

        # =====================================================
        # Skills Comparison
        # =====================================================

        st.header("🛠️ Skills Comparison")

        col1, col2, col3 = st.columns(3)

        # -----------------------------
        # Matched Skills
        # -----------------------------

        with col1:

            st.subheader("✅ Matched")

            if ats_result.matched_skills:

                for skill in ats_result.matched_skills:
                    st.success(skill)

            else:

                st.warning("No matched skills.")

        # -----------------------------
        # Missing Skills
        # -----------------------------

        with col2:

            st.subheader("❌ Missing")

            if ats_result.missing_skills:

                for skill in ats_result.missing_skills:
                    st.error(skill)

            else:

                st.success("No missing skills.")

        # -----------------------------
        # Additional Skills
        # -----------------------------

        with col3:

            st.subheader("⭐ Additional")

            if ats_result.additional_skills:

                for skill in ats_result.additional_skills:
                    st.info(skill)

            else:

                st.warning("No additional skills.")

        st.divider()

        # =====================================================
        # Resume Information
        # =====================================================

        st.header("👤 Candidate Information")

        info1, info2 = st.columns(2)

        with info1:

            st.write(
                f"**Name:** {resume_data.personal_info.name}"
            )

            st.write(
                f"**Email:** {resume_data.personal_info.email}"
            )

        with info2:

            st.write(
                f"**Phone:** {resume_data.personal_info.phone}"
            )

            st.write(
                f"**Location:** {resume_data.personal_info.location}"
            )

        st.divider()

        # =====================================================
        # Resume Preview
        # =====================================================

        with st.expander(
            "📄 Resume Preview",
            expanded=False,
        ):

            st.text_area(
                label="",
                value=resume_text[:MAX_PREVIEW_CHARS],
                height=350,
            )

    except Exception as error:

        st.error(
            "❌ An error occurred while processing the uploaded files."
        )

        st.exception(error)
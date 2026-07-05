import streamlit as st

from components.uploader import save_uploaded_file
from utils.parser import extract_pdf_data
from services.resume_service import ResumeService


def show_dashboard():
    """
    Render the main dashboard.
    """

    st.title("💼 HireMate")
    st.subheader("AI-Powered Resume & Job Matching Assistant")

    st.write(
        "Upload your Resume and Job Description to begin AI-powered evaluation."
    )

    st.divider()

    col1, col2 = st.columns(2)

    # ==========================================================
    # Resume Upload
    # ==========================================================

    with col1:

        st.markdown("### 📄 Resume")

        resume = st.file_uploader(
            "Upload Resume",
            type=["pdf"],
            key="resume",
        )

        if resume:

            # Save uploaded file
            file_path = save_uploaded_file(resume)

            # Extract raw PDF data
            pdf_data = extract_pdf_data(file_path)

            # Parse structured resume information
            resume_data = ResumeService().parse(pdf_data["text"])

            st.success("✅ Resume uploaded successfully!")

            # -------------------------
            # PDF Statistics
            # -------------------------

            st.subheader("📊 Document Statistics")

            stat1, stat2, stat3 = st.columns(3)

            stat1.metric("Pages", pdf_data["pages"])
            stat2.metric("Words", pdf_data["words"])
            stat3.metric("Characters", pdf_data["characters"])

            st.divider()

            # -------------------------
            # Personal Information
            # -------------------------

            st.subheader("👤 Personal Information")

            info1, info2 = st.columns(2)

            with info1:
                st.write(f"**Name:** {resume_data.personal_info.name}")
                st.write(f"**Email:** {resume_data.personal_info.email}")

            with info2:
                st.write(f"**Phone:** {resume_data.personal_info.phone}")
                st.write(f"**Location:** {resume_data.personal_info.location}")

            st.divider()

            # -------------------------
            # Skills
            # -------------------------

            st.subheader("🛠️ Detected Skills")

            if resume_data.skills:

                cols = st.columns(3)

                for index, skill in enumerate(resume_data.skills):
                    cols[index % 3].success(skill)

            else:

                st.warning("No skills detected.")

            st.divider()

            # -------------------------
            # Resume Preview
            # -------------------------

            with st.expander("📄 Resume Preview", expanded=False):

                st.text_area(
                    label="",
                    value=pdf_data["text"][:3000],
                    height=350,
                )

    # ==========================================================
    # Job Description Upload
    # ==========================================================

    with col2:

        st.markdown("### 💼 Job Description")

        jd = st.file_uploader(
            "Upload Job Description",
            type=["pdf", "txt"],
            key="jd",
        )

        if jd:

            st.success("✅ Job Description uploaded successfully!")

            st.info(
                "Job Description parsing will be implemented in the next sprint."
            )
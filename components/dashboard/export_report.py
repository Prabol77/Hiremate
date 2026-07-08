"""
Dashboard Export Report.
"""

from services.export_service import ExportService
from services.report_service import ReportService

import streamlit as st


def render_export_report(
    *,
    candidate_name,
    ats_result,
    review,
    recommendations,
    interview,
    cover_letter,
):
    """
    Render report export section.
    """

    st.divider()

    st.subheader("📥 Export Report")

    report = ReportService.generate_report(

        candidate_name=candidate_name,

        ats_score=ats_result.overall_score,

        skills_found=ats_result.matched_skills,

        skills_missing=ats_result.missing_skills,

        review=review,

        recommendations=recommendations,

        interview_questions=getattr(
            interview,
            "technical_questions",
            [],
        ),

        cover_letter=cover_letter,
    )

    txt = ExportService.export_txt(
        report,
    )

    docx = ExportService.export_docx(
        "HireMate Report",
        report,
    )

    pdf = ExportService.export_pdf(
        "HireMate Report",
        report,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(

            "📝 TXT",

            txt,

            "HireMate_Report.txt",

            "text/plain",

            use_container_width=True,

        )

    with col2:

        st.download_button(

            "📄 DOCX",

            docx,

            "HireMate_Report.docx",

            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

            use_container_width=True,

        )

    with col3:

        st.download_button(

            "📑 PDF",

            pdf,

            "HireMate_Report.pdf",

            "application/pdf",

            use_container_width=True,

        )
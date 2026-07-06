import os
from datetime import datetime

import streamlit as st

from services.report_service import ReportService


def render_export_button(
    resume_data,
    ats_result,
    review,
    recommendations,
    interview,
):
    """
    Render the PDF report export section.
    """

    st.subheader("📄 Export Analysis Report")

    if st.button(
        "📥 Generate PDF Report",
        use_container_width=True,
    ):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_dir = "generated_reports"

        os.makedirs(
            output_dir,
            exist_ok=True,
        )

        output_path = os.path.join(
            output_dir,
            f"HireMate_Report_{timestamp}.pdf",
        )

        try:

            with st.spinner("Generating PDF report..."):

                ReportService().generate(
                    output_path=output_path,
                    resume_data=resume_data,
                    ats_result=ats_result,
                    review=review,
                    recommendations=recommendations,
                    interview=interview,
                )

            st.success("✅ PDF report generated successfully!")

            with open(
                output_path,
                "rb",
            ) as pdf:

                st.download_button(
                    label="⬇ Download Report",
                    data=pdf,
                    file_name=os.path.basename(output_path),
                    mime="application/pdf",
                    use_container_width=True,
                )

        except Exception as exc:

            st.error("Failed to generate the PDF report.")

            st.exception(exc)

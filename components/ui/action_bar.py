"""
Reusable action bar for exporting generated documents.
"""

import streamlit as st


def render_action_bar(
    *,
    txt_data: bytes | None = None,
    docx_data: bytes | None = None,
    pdf_data: bytes | None = None,
    base_filename: str = "HireMate_Document",
):
    """
    Render export buttons.

    Parameters
    ----------
    txt_data:
        TXT file bytes.

    docx_data:
        DOCX file bytes.

    pdf_data:
        PDF file bytes.

    base_filename:
        Filename without extension.
    """

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        if txt_data is not None:

            st.download_button(
                label="📝 TXT",
                data=txt_data,
                file_name=f"{base_filename}.txt",
                mime="text/plain",
                use_container_width=True,
            )

    with col2:

        if docx_data is not None:

            st.download_button(
                label="📄 DOCX",
                data=docx_data,
                file_name=f"{base_filename}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )

    with col3:

        if pdf_data is not None:

            st.download_button(
                label="📑 PDF",
                data=pdf_data,
                file_name=f"{base_filename}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
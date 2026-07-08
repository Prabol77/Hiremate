"""
Cover Letter Tab.

Displays the AI-generated cover letter
and provides export options.
"""

from models.cover_letter_model import (
    CoverLetterResult,
)

from services.export_service import (
    ExportService,
)

from components.ui.section_header import (
    render_section_header,
)

from components.ui.document_preview import (
    render_document_preview,
)

from components.ui.action_bar import (
    render_action_bar,
)


def render_cover_letter_tab(
    cover_letter: CoverLetterResult,
):
    """
    Render the Cover Letter tab.
    """

    render_section_header(
        "📄 AI Cover Letter",
        "Professionally generated cover letter based on your resume and the job description.",
    )

    if not cover_letter or not cover_letter.full_letter:

        render_document_preview(
            "Cover Letter",
            "No cover letter generated.",
        )

        return

    render_document_preview(
        "Cover Letter",
        cover_letter.full_letter,
    )

    txt_data = ExportService.export_txt(
        cover_letter.full_letter,
    )

    docx_data = ExportService.export_docx(
        "HireMate Cover Letter",
        cover_letter.full_letter,
    )

    pdf_data = ExportService.export_pdf(
        "HireMate Cover Letter",
        cover_letter.full_letter,
    )

    render_action_bar(
        txt_data=txt_data,
        docx_data=docx_data,
        pdf_data=pdf_data,
        base_filename="HireMate_Cover_Letter",
    )
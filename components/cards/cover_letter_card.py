"""
Cover Letter Card.

Displays the AI-generated cover letter with export options.
"""

from services.export_service import ExportService
from models.cover_letter_model import CoverLetterResult

from components.ui.action_bar import render_action_bar
from components.ui.info_badge import render_info_badge
from components.ui.section_header import render_section_header
from components.ui.document_preview import (
    render_document_preview,
)


def render_cover_letter_card(
    cover_letter: CoverLetterResult,
):
    """
    Render the AI-generated cover letter.
    """

    # =====================================================
    # Header
    # =====================================================

    render_section_header(
        title="📄 AI Cover Letter",
        subtitle=(
            "Professionally generated using your "
            "resume and the selected job description."
        ),
    )

    # =====================================================
    # Information
    # =====================================================

    company_col, position_col = render_columns()

    with company_col:

        render_info_badge(
            "🏢 Company",
            cover_letter.company_name,
        )

    with position_col:

        render_info_badge(
            "💼 Position",
            cover_letter.position,
        )

    # =====================================================
    # Build Letter
    # =====================================================

    letter = build_cover_letter(
        cover_letter,
    )

    # =====================================================
    # Preview
    # =====================================================

    render_document_preview(
        "📋 Cover Letter",
        letter,
    )

    # =====================================================
    # Export
    # =====================================================

    render_action_bar(
        txt_data=ExportService.export_txt(
            letter,
        ),

        docx_data=ExportService.export_docx(
            "HireMate AI Cover Letter",
            letter,
        ),

        pdf_data=ExportService.export_pdf(
            "HireMate AI Cover Letter",
            letter,
        ),

        base_filename="HireMate_Cover_Letter",
    )

import streamlit as st


def render_columns():
    """
    Render two responsive columns.
    """

    return st.columns(2)


def build_cover_letter(
    cover_letter: CoverLetterResult,
) -> str:
    """
    Build the final cover letter text.
    """

    if cover_letter.full_letter.strip():

        return cover_letter.full_letter.strip()

    return "\n\n".join(

        filter(
            None,
            [
                cover_letter.greeting,

                cover_letter.introduction,

                cover_letter.body,

                cover_letter.conclusion,

                cover_letter.closing,
            ],
        )

    )
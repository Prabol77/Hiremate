"""
Dashboard Summary Card.
"""

from components.ui.document_preview import (
    render_document_preview,
)

from components.ui.section_header import (
    render_section_header,
)


def render_summary_card(
    summary: str,
):
    """
    Render resume summary.
    """

    render_section_header(
        "📄 Resume Summary",
        "AI-generated summary of the candidate profile.",
    )

    render_document_preview(
        "Summary",
        summary,
    )
"""
Dashboard Upload Module.

Responsibilities:
- Render upload widgets
- Save uploaded files
- Extract resume and job description text
"""

from typing import Tuple

import streamlit as st

from components.uploader import save_uploaded_file
from config import (
    SUPPORTED_JD_TYPES,
    SUPPORTED_RESUME_TYPES,
)
from utils.parser import extract_pdf_data


# ==========================================================
# Upload Section
# ==========================================================


def render_upload_section():
    """
    Render the resume and job description upload widgets.

    Returns:
        tuple:
            (
                Uploaded Resume,
                Uploaded Job Description,
            )
    """

    left, right = st.columns(2)

    with left:

        resume = st.file_uploader(
            "📄 Upload Resume",
            type=SUPPORTED_RESUME_TYPES,
            key="resume",
        )

    with right:

        jd = st.file_uploader(
            "💼 Upload Job Description",
            type=SUPPORTED_JD_TYPES,
            key="jd",
        )

    return resume, jd


# ==========================================================
# Document Loader
# ==========================================================


def load_documents(
    resume,
    jd,
) -> Tuple[dict, str, str]:
    """
    Load uploaded resume and job description.

    Returns:
        (
            resume_pdf,
            resume_text,
            jd_text,
        )
    """

    resume.seek(0)
    jd.seek(0)

    resume_path = save_uploaded_file(
        resume,
    )

    jd_path = save_uploaded_file(
        jd,
    )

    # ------------------------------------------------------
    # Resume
    # ------------------------------------------------------

    resume_pdf = extract_pdf_data(
        resume_path,
    )

    resume_text = resume_pdf["text"]

    # ------------------------------------------------------
    # Job Description
    # ------------------------------------------------------

    if jd.name.lower().endswith(".pdf"):

        jd_pdf = extract_pdf_data(
            jd_path,
        )

        jd_text = jd_pdf["text"]

    else:

        with open(
            jd_path,
            "r",
            encoding="utf-8",
        ) as file:

            jd_text = file.read()

    return (
        resume_pdf,
        resume_text,
        jd_text,
    )
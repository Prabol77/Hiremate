"""
AI Resume Rewrite Service.
"""

import json
import streamlit as st

from models.rewrite_model import (
    RewriteResult,
)

from services.groq_service import (
    GroqService,
)

from utils.prompts import (
    REWRITE_SYSTEM_PROMPT,
    rewrite_prompt,
)


class RewriteService:
    """
    AI Resume Rewrite Service.
    """

    def __init__(self):

        self.groq = GroqService()

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        resume_text: str,
        jd_text: str,
    ) -> RewriteResult:
        """
        Generate an ATS-optimized resume rewrite.
        """

        prompt = rewrite_prompt(
            resume_text,
            jd_text,
        )

        try:

            response = self.groq.chat(
                REWRITE_SYSTEM_PROMPT,
                prompt,
            )

            # Remove markdown code fences if present
            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(response)

            result = RewriteResult()

            result.professional_summary = data.get(
                "professional_summary",
                "",
            )

            result.experience = data.get(
                "experience",
                "",
            )

            result.projects = data.get(
                "projects",
                "",
            )

            result.skills = data.get(
                "skills",
                "",
            )

            result.suggestions = data.get(
                "suggestions",
                [],
            )

            result.ats_improvement = data.get(
                "ats_improvement",
                "",
            )

            return result

        except Exception as error:

            st.error(
                "Resume Rewrite generation failed."
            )

            st.exception(error)

            return self._default_result()

    # =====================================================
    # Default Result
    # =====================================================

    def _default_result(
        self,
    ) -> RewriteResult:
        """
        Return a fallback response.
        """

        result = RewriteResult()

        result.professional_summary = (
            "Unable to generate an optimized professional summary."
        )

        result.experience = (
            "Unable to rewrite the experience section."
        )

        result.projects = (
            "Unable to rewrite the projects section."
        )

        result.skills = (
            "Unable to optimize the skills section."
        )

        result.suggestions = [
            "Use action verbs.",
            "Quantify achievements where possible.",
            "Align keywords with the job description.",
        ]

        result.ats_improvement = (
            "Review your resume manually and add relevant keywords from the job description."
        )

        return result
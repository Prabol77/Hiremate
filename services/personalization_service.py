"""
AI Personalization Service.
"""

import json

from models.personalization_model import (
    PersonalizationResult,
)

from services.groq_service import (
    GroqService,
)

from utils.prompts import (
    PERSONALIZATION_SYSTEM_PROMPT,
    personalization_prompt,
)


class PersonalizationService:
    """
    Generate AI-powered personalized explanations.
    """

    def __init__(self):

        self.groq = GroqService()

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        resume_data,
        career,
        hireability,
        projects,
        companies,
        certifications,
    ) -> PersonalizationResult:
        """
        Generate personalized AI insights.
        """

        fallback = self._default_result(
            career,
            hireability,
        )

        prompt = personalization_prompt(
            resume_data,
            career,
            hireability,
            projects,
            companies,
            certifications,
        )

        try:

            response = self.groq.chat(
                PERSONALIZATION_SYSTEM_PROMPT,
                prompt,
            )

            data = json.loads(
                response,
            )

            result = PersonalizationResult()

            result.career_summary = data.get(
                "career_summary",
                fallback.career_summary,
            )

            result.why_projects = data.get(
                "why_projects",
                fallback.why_projects,
            )

            result.why_certifications = data.get(
                "why_certifications",
                fallback.why_certifications,
            )

            result.why_companies = data.get(
                "why_companies",
                fallback.why_companies,
            )

            result.final_advice = data.get(
                "final_advice",
                fallback.final_advice,
            )

            return result

        except Exception:

            return fallback

    # =====================================================
    # Default Result
    # =====================================================

    def _default_result(
        self,
        career,
        hireability,
    ) -> PersonalizationResult:
        """
        Deterministic fallback.
        """

        result = PersonalizationResult()

        result.career_summary = (
            f"You are currently progressing toward a "
            f"{career.target_role} role with a "
            f"Hireability Score of {hireability.overall}%."
        )

        result.why_projects = (
            "Recommended projects are selected to "
            "strengthen practical experience and "
            "improve your portfolio."
        )

        result.why_certifications = (
            "The suggested certifications address "
            "your current skill gaps and improve "
            "industry recognition."
        )

        result.why_companies = (
            "Company matches are based on your "
            "current skills, ATS performance, and "
            "overall Hireability Score."
        )

        result.final_advice = (
            "Focus on consistent learning, build "
            "real-world projects, and update your "
            "resume regularly."
        )

        return result
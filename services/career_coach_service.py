"""
Career Coach Service.
"""

import json

from models.career_coach_model import (
    CareerCoachResult,
)

from services.groq_service import (
    GroqService,
)

from utils.career_coach_prompt import (
    CAREER_COACH_SYSTEM_PROMPT,
    career_coach_prompt,
)


class CareerCoachService:
    """
    Generates personalized career coaching.
    """

    def __init__(self):

        self.groq = GroqService()

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        resume_data,
        ats_result,
        career,
        hireability,
        projects,
    ) -> CareerCoachResult:
        """
        Generate AI-powered career coaching.
        Falls back to deterministic coaching if AI fails.
        """

        fallback = self._default_result(
            ats_result,
            career,
            hireability,
            projects,
        )

        prompt = career_coach_prompt(
            resume_data,
            ats_result,
            career,
            hireability,
            projects,
        )

        try:

            response = self.groq.chat(
                CAREER_COACH_SYSTEM_PROMPT,
                prompt,
            )

            data = json.loads(
                response,
            )

            result = CareerCoachResult()

            result.summary = data.get(
                "summary",
                fallback.summary,
            )

            result.strengths = data.get(
                "strengths",
                fallback.strengths,
            )

            result.focus_areas = data.get(
                "focus_areas",
                fallback.focus_areas,
            )

            result.weekly_goals = data.get(
                "weekly_goals",
                fallback.weekly_goals,
            )

            result.recommended_projects = data.get(
                "recommended_projects",
                fallback.recommended_projects,
            )

            result.recommended_certifications = data.get(
                "recommended_certifications",
                fallback.recommended_certifications,
            )

            result.interview_strategy = data.get(
                "interview_strategy",
                fallback.interview_strategy,
            )

            result.final_message = data.get(
                "final_message",
                fallback.final_message,
            )

            return result

        except Exception:

            return fallback

    # =====================================================
    # Default Coaching
    # =====================================================

    def _default_result(
        self,
        ats_result,
        career,
        hireability,
        projects,
    ) -> CareerCoachResult:
        """
        Deterministic fallback coaching.
        """

        result = CareerCoachResult()

        result.summary = (
            f"Your current Hireability Score is "
            f"{hireability.overall}%. "
            f"You are progressing toward becoming a "
            f"{career.target_role}. "
            "Focus on improving your missing skills "
            "and completing practical projects."
        )

        result.strengths = (
            ats_result.strengths[:3]
        )

        result.focus_areas = (
            ats_result.weaknesses[:3]
        )

        result.weekly_goals = [

            "Complete Week 1 of your learning roadmap.",

            "Practice at least 20 interview questions.",

            "Update your resume after completing a project.",

        ]

        result.recommended_projects = [

            project.title

            for project in projects[:3]

        ]

        result.recommended_certifications = [

            "AWS Cloud Practitioner",

            "Google Cybersecurity",

            "Microsoft Azure Fundamentals",

        ]

        result.interview_strategy = [

            "Revise core technical concepts.",

            "Prepare to explain your projects clearly.",

            "Practice behavioral interview questions.",

        ]

        result.final_message = (

            "Consistency beats intensity. "
            "Improve one skill every week and your "
            "Hireability Score will steadily increase."

        )

        return result
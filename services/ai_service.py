import json

from models.recommendation_model import RecommendationResult
from models.review_model import ReviewResult
from models.rewrite_model import RewriteResult
from services.groq_service import GroqService
from utils.prompts import (
    RECOMMENDATION_SYSTEM_PROMPT,
    REVIEW_SYSTEM_PROMPT,
    REWRITE_SYSTEM_PROMPT,
    recommendation_prompt,
    review_prompt,
    rewrite_prompt,
)


class AIService:
    """
    Central AI service for HireMate.

    Responsibilities:
    - AI Resume Review
    - AI Resume Rewrite
    - AI Recommendations

    Future:
    - AI Interview Questions
    - Cover Letter Generation
    - Learning Roadmap
    """

    def __init__(self):
        self.groq = GroqService()

    # ======================================================
    # Resume Review
    # ======================================================

    def generate_review(
        self,
        resume_text: str,
        jd_text: str,
    ) -> ReviewResult:
        """
        Generate AI-powered resume review.
        """

        prompt = review_prompt(
            resume_text,
            jd_text,
        )

        response = self.groq.chat(
            REVIEW_SYSTEM_PROMPT,
            prompt,
        )

        result = ReviewResult()

        try:

            data = json.loads(response)

            result.summary = data.get(
                "summary",
                "",
            )

            result.strengths = data.get(
                "strengths",
                [],
            )

            result.weaknesses = data.get(
                "weaknesses",
                [],
            )

            result.recommendations = data.get(
                "recommendations",
                [],
            )

        except Exception:

            result.summary = response

        return result

    # ======================================================
    # Resume Rewrite
    # ======================================================

    def rewrite_resume(
        self,
        section_name: str,
        section_text: str,
        jd_text: str,
    ) -> RewriteResult:
        """
        Rewrite a specific resume section using AI.
        """

        prompt = rewrite_prompt(
            section_name,
            section_text,
            jd_text,
        )

        response = self.groq.chat(
            REWRITE_SYSTEM_PROMPT,
            prompt,
        )

        result = RewriteResult()

        result.section_name = section_name

        try:

            data = json.loads(response)

            result.original_text = data.get(
                "original_text",
                section_text,
            )

            result.improved_text = data.get(
                "improved_text",
                "",
            )

            result.explanation = data.get(
                "explanation",
                "",
            )

            result.estimated_improvement = data.get(
                "estimated_improvement",
                "",
            )

        except Exception:

            result.original_text = section_text
            result.improved_text = response
            result.explanation = (
                "Unable to parse AI response."
            )
            result.estimated_improvement = "N/A"

        return result

    # ======================================================
    # AI Recommendations
    # ======================================================

    def generate_recommendations(
        self,
        resume_text: str,
        jd_text: str,
    ) -> RecommendationResult:
        """
        Generate AI-powered recommendations.
        """

        prompt = recommendation_prompt(
            resume_text,
            jd_text,
        )

        response = self.groq.chat(
            RECOMMENDATION_SYSTEM_PROMPT,
            prompt,
        )

        result = RecommendationResult()

        try:

            data = json.loads(response)

            result.ats_optimization = data.get(
                "ats_optimization",
                [],
            )

            result.skills_to_learn = data.get(
                "skills_to_learn",
                [],
            )

            result.resume_improvements = data.get(
                "resume_improvements",
                [],
            )

            result.next_steps = data.get(
                "next_steps",
                [],
            )

        except Exception:

            result.ats_optimization = []
            result.skills_to_learn = []
            result.resume_improvements = []
            result.next_steps = []

        return result
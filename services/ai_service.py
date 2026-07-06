import json

from models.review_model import ReviewResult

from services.groq_service import GroqService

from utils.prompts import (
    REVIEW_SYSTEM_PROMPT,
    review_prompt,
)


class AIService:
    """
    Generates AI-powered resume review.
    """

    def __init__(self):

        self.groq = GroqService()

    def generate_review(
        self,
        resume_text: str,
        jd_text: str,
    ) -> ReviewResult:

        prompt = review_prompt(
            resume_text,
            jd_text,
        )

        response = self.groq.chat(
            REVIEW_SYSTEM_PROMPT,
            prompt,
        )

        review = ReviewResult()

        try:

            data = json.loads(
                response
            )

            review.summary = data.get(
                "summary",
                "",
            )

            review.strengths = data.get(
                "strengths",
                [],
            )

            review.weaknesses = data.get(
                "weaknesses",
                [],
            )

            review.recommendations = data.get(
                "recommendations",
                [],
            )

        except Exception:

            review.summary = response

        return review
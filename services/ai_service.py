import json
from models.cover_letter_model import CoverLetterResult
from models.recommendation_model import RecommendationResult
from models.review_model import ReviewResult
from models.rewrite_model import RewriteResult
from services.groq_service import GroqService

from utils.prompts import (
    COVER_LETTER_SYSTEM_PROMPT,
    cover_letter_prompt,
    REVIEW_SYSTEM_PROMPT,
    review_prompt,
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
# Internal Helpers
# ======================================================

    def _chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Send a prompt to Groq.
        """

        return self.groq.chat(
            system_prompt,
            user_prompt,
        )


    def _generate_json(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:
        """
        Generate and parse JSON.
        """

        from utils.json_parser import (
            parse_llm_json,
        )

        response = self._chat(
            system_prompt,
            user_prompt,
        )

        return parse_llm_json(
            response,
        )

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
        
# ======================================================
# AI Cover Letter
# ======================================================

    def generate_cover_letter(
        self,
        resume_text: str,
        jd_text: str,
        style: str = "Professional",
    ) -> CoverLetterResult:
        
        """
        Generate an AI-powered cover letter.
        """
        prompt = cover_letter_prompt(
            resume_text,
            jd_text,
            style,
        )

        response = self.groq.chat(
            COVER_LETTER_SYSTEM_PROMPT,
            prompt,
        )

        result = CoverLetterResult()

        try:

            cleaned = response.strip()

            if cleaned.startswith("```json"):
                cleaned = cleaned.replace("```json", "", 1)

            if cleaned.startswith("```"):
                cleaned = cleaned.replace("```", "", 1)

            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]

            cleaned = cleaned.strip()

            data = json.loads(cleaned)

            result.company_name = data.get(
                "company_name",
                "Unknown",
            )

            result.position = data.get(
                "position",
                "Unknown",
            )

            result.greeting = data.get(
                "greeting",
                "",
            )

            result.introduction = data.get(
                "introduction",
                "",
            )

            result.body = data.get(
                "body",
                "",
            )

            result.conclusion = data.get(
                "conclusion",
                "",
            )

            result.closing = data.get(
                "closing",
                "",
            )

            result.full_letter = data.get(
                "full_letter",
                "",
            )

            # Build the letter if full_letter is empty
            if not result.full_letter:

                result.full_letter = "\n\n".join(
                    filter(
                        None,
                        [
                            result.greeting,
                            result.introduction,
                            result.body,
                            result.conclusion,
                            result.closing,
                        ],
                    )
                )

        except Exception as e:

            print("Cover Letter Parsing Error:", e)
            print(response)

            result.company_name = "Unknown"
            result.position = "Unknown"
            result.full_letter = response

        return result
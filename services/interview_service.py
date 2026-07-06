import json

from models.interview_model import InterviewResult
from services.groq_service import GroqService
from utils.prompts import INTERVIEW_SYSTEM_PROMPT, interview_prompt


class InterviewService:
    """
    Generates AI-powered interview questions based on
    the candidate's resume and job description.
    """

    def __init__(self):

        self.groq = GroqService()

    # =====================================================
    # Interview Question Generation
    # =====================================================

    def generate(
        self,
        resume_text: str,
        jd_text: str,
    ) -> InterviewResult:
        """
        Generate categorized interview questions.

        Returns:
            InterviewResult
        """

        prompt = interview_prompt(
            resume_text,
            jd_text,
        )

        response = self.groq.chat(
            INTERVIEW_SYSTEM_PROMPT,
            prompt,
        )

        result = InterviewResult()

        try:

            data = json.loads(response)

            result.questions = data.get(
                "questions",
                {},
            )

            result.overall_tips = data.get(
                "overall_tips",
                [],
            )

        except json.JSONDecodeError:

            result.questions = {
                "AI Response": [
                    "Unable to parse AI response.",
                ]
            }

            result.overall_tips = ["Please try generating interview questions again."]

        return result

import json

from models.interview_model import InterviewResult

from services.groq_service import GroqService

from utils.prompts import (
    INTERVIEW_SYSTEM_PROMPT,
    interview_prompt,
)


class InterviewService:
    """
    Generates AI interview questions using Groq.
    """

    def __init__(self):

        self.groq = GroqService()

    def generate(
        self,
        resume_text: str,
        jd_text: str,
    ) -> InterviewResult:

        response = self.groq.chat(

            INTERVIEW_SYSTEM_PROMPT,

            interview_prompt(
                resume_text,
                jd_text,
            ),

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

        except Exception:

            result.questions = {

                "AI Error": [

                    response

                ]

            }

        return result
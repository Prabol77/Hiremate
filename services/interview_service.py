import json
import re

from models.interview_model import InterviewResult

from services.groq_service import GroqService

from utils.interview_prompt import (
    INTERVIEW_SYSTEM_PROMPT,
    interview_prompt,
)


class InterviewService:
    """
    Generate AI interview questions.
    """

    def __init__(self):

        self.groq = GroqService()

    # =====================================================

    def _extract_json(
        self,
        response: str,
    ):
        """
        Extract JSON from AI response.
        """

        response = response.strip()

        # Remove markdown fences
        response = re.sub(
            r"^```(?:json)?",
            "",
            response,
            flags=re.IGNORECASE,
        )

        response = re.sub(
            r"```$",
            "",
            response,
        ).strip()

        # Find JSON object
        match = re.search(
            r"\{.*\}",
            response,
            flags=re.DOTALL,
        )

        if match:

            response = match.group(0)

        return json.loads(response)

    # =====================================================

    def generate(
        self,
        resume_data,
        jd_text: str,
    ) -> InterviewResult:

        prompt = interview_prompt(
            resume_data,
            jd_text,
        )

        response = self.groq.chat(
            INTERVIEW_SYSTEM_PROMPT,
            prompt,
        )
        print("\n========== GROQ RESPONSE ==========")
        print(response)
        print("===================================\n")

        result = InterviewResult()

        try:

            data = self._extract_json(
                response,
            )

            result.questions = data.get(
                "questions",
                {},
            )

            result.overall_tips = data.get(
                "overall_tips",
                [],
            )

        except Exception as e:

            print("Interview Parser Error:")
            print(e)

            print("\nRaw Response:\n")
            print(response)

            result.questions = {
                "AI Response": [
                    "Unable to parse AI response."
                ]
            }

            result.overall_tips = [
                "Please try generating interview questions again."
            ]

        return result
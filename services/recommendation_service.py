"""
Recommendation Service.
"""

from models.recommendation_model import RecommendationResult


class RecommendationService:
    """
    Generates personalized recommendations based on
    resume metadata and ATS analysis.
    """

    def generate(
        self,
        resume_data,
        ats_result,
    ) -> RecommendationResult:

        result = RecommendationResult()

        self._technical(
            resume_data,
            ats_result,
            result,
        )

        self._resume(
            resume_data,
            ats_result,
            result,
        )

        self._career(
            resume_data,
            ats_result,
            result,
        )

        return result

    # =====================================================

    def _technical(
        self,
        resume_data,
        ats_result,
        result,
    ):

        domain = resume_data.metadata.get(
            "primary_domain",
            "General",
        )

        if ats_result.missing_skills:

            result.technical.append(
                "Learn: "
                + ", ".join(
                    ats_result.missing_skills[:5]
                )
            )

        if domain == "AI/ML":

            result.technical.append(
                "Build an end-to-end ML deployment project."
            )

        elif domain == "Web Development":

            result.technical.append(
                "Deploy a full-stack application online."
            )

        elif domain == "Data Science":

            result.technical.append(
                "Create an interactive analytics dashboard."
            )

        elif domain == "DevOps":

            result.technical.append(
                "Build a CI/CD deployment pipeline."
            )

    # =====================================================

    def _resume(
        self,
        resume_data,
        ats_result,
        result,
    ):

        if ats_result.projects_score < 70:

            result.resume.append(
                "Add more practical projects."
            )

        if ats_result.experience_score < 70:

            result.resume.append(
                "Include internships or freelance experience."
            )

        if ats_result.completeness_score < 100:

            result.resume.append(
                "Complete all personal information."
            )

        result.resume.append(
            "Use measurable achievements whenever possible."
        )

    # =====================================================

    def _career(
        self,
        resume_data,
        ats_result,
        result,
    ):

        domain = resume_data.metadata.get(
            "primary_domain",
            "General",
        )

        if domain == "AI/ML":

            result.career.extend(
                [
                    "Participate in Kaggle competitions.",
                    "Learn MLOps fundamentals.",
                ]
            )

        elif domain == "Web Development":

            result.career.extend(
                [
                    "Build a portfolio website.",
                    "Contribute to open-source web projects.",
                ]
            )

        elif domain == "Data Science":

            result.career.extend(
                [
                    "Practice SQL interview questions.",
                    "Create data visualization projects.",
                ]
            )

        elif domain == "DevOps":

            result.career.extend(
                [
                    "Learn Kubernetes.",
                    "Earn an AWS certification.",
                ]
            )
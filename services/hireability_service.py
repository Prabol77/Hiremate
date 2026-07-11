from models.hireability_model import (
    HireabilityScore,
)


class HireabilityService:
    """
    Calculates the overall Hireability Score.
    """

    def generate(
        self,
        ats_result,
        career,
    ) -> HireabilityScore:

        score = HireabilityScore()

        score.resume = int(
            ats_result.completeness_score
        )

        score.ats = int(
            ats_result.overall_score
        )

        score.technical = int(
            ats_result.skills_score
        )

        score.projects = int(
            ats_result.projects_score
        )

        score.career = int(
            career.readiness_score
        )

        # Placeholder until Interview Intelligence
        # becomes more sophisticated.

        score.interview = int(
            career.readiness_score * 0.9
        )

        values = [
            score.resume,
            score.ats,
            score.technical,
            score.projects,
            score.career,
            score.interview,
        ]

        score.overall = sum(values) // len(values)

# ==================================================
# Grade
# ==================================================

        if score.overall >= 90:
            score.grade = "A+"

        elif score.overall >= 80:

            score.grade = "A"

        elif score.overall >= 70:

            score.grade = "B"

        elif score.overall >= 60:

            score.grade = "C"

        else:

            score.grade = "D"

# ==================================================
# Improvement Potential
# ==================================================

        score.improvement_potential = (
            100 - score.overall
        )

# ==================================================
# Insights
# ==================================================

        score.strengths = (
            ats_result.strengths[:3]
            if ats_result.strengths
            else ["Keep building your strengths."]
        )

        score.weaknesses = (
            ats_result.weaknesses[:3]
            if ats_result.weaknesses
            else ["No major weaknesses detected."]
        )

        score.next_actions = [

            "Improve your missing technical skills.",

            "Complete your learning roadmap.",

            "Practice interview questions.",

        ]

        return score
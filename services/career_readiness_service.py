from models.career_readiness_model import (
    CareerReadiness,
)


class CareerReadinessService:
    """
    Calculates career readiness based on ATS
    and learning roadmap.
    """

    def generate(
        self,
        ats_result,
        roadmap,
    ) -> CareerReadiness:

        result = CareerReadiness()

        score = int(
            ats_result.overall_score
        )

        result.score = score

        if score >= 90:

            result.stage = "💎 Industry Ready"

            result.confidence = "Very High"

        elif score >= 80:

            result.stage = "🏆 Competitive"

            result.confidence = "High"

        elif score >= 70:

            result.stage = "🚀 Job Ready"

            result.confidence = "Moderate"

        elif score >= 55:

            result.stage = "🌿 Emerging Developer"

            result.confidence = "Growing"

        else:

            result.stage = "🌱 Beginner"

            result.confidence = "Low"

        result.summary = (

            f"Your resume currently matches "
            f"{score}% of the target job requirements."

        )

        result.estimated_duration = (

            f"{roadmap.duration_weeks} Weeks"

        )

        return result
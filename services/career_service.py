from models.career_model import (
    CareerGoal,
)


class CareerService:
    """
    Generates a career readiness summary.
    """

    def generate(
        self,
        resume_data,
        ats_result,
        roadmap,
    ) -> CareerGoal:

        career = CareerGoal()

        career.current_level = "Student"

        career.target_role = (
            resume_data.metadata.get(
                "primary_domain",
                "Software Engineer",
            )
        )

        career.readiness_score = int(
            ats_result.overall_score
        )

        career.estimated_duration = (
            f"{roadmap.duration_weeks} Weeks"
        )

        career.strengths = ats_result.strengths[:5]

        career.focus_areas = [
            task.title
            for task in roadmap.tasks[:5]
        ]

        return career
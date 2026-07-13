from models.career_intelligence_model import (
    CareerIntelligence,
)


class CareerIntelligenceService:
    """
    Generates a unified career intelligence report
    using resume analysis, ATS results, skill gaps,
    and the personalized learning roadmap.
    """

    def generate(
        self,
        resume_data,
        ats_result,
        skill_gap,
        roadmap,
    ) -> CareerIntelligence:

        career = CareerIntelligence()

        # ==================================================
        # Candidate Information
        # ==================================================

        career.current_role = "Student"

        career.target_role = resume_data.metadata.get(
            "primary_domain",
            "Software Engineer",
        )

        # ==================================================
        # Readiness Score
        # ==================================================

        score = int(
            ats_result.overall_score
        )

        career.readiness_score = score

        # ==================================================
        # Career Stage
        # ==================================================

        if score >= 90:

            career.stage = "💎 Industry Ready"

            career.confidence = "Very High"

        elif score >= 80:

            career.stage = "🏆 Competitive"

            career.confidence = "High"

        elif score >= 70:

            career.stage = "🚀 Job Ready"

            career.confidence = "Moderate"

        elif score >= 55:

            career.stage = "🌿 Emerging Developer"

            career.confidence = "Growing"

        else:

            career.stage = "🌱 Beginner"

            career.confidence = "Low"

        # ==================================================
        # Summary
        # ==================================================

        career.summary = (
            f"Your resume currently matches approximately "
            f"{score}% of the target job requirements."
        )

        # ==================================================
        # Learning Timeline
        # ==================================================

        career.estimated_duration = (
            f"{roadmap.duration_weeks} Weeks"
        )

        # ==================================================
        # Strengths
        # ==================================================

        career.strengths = (
            ats_result.strengths[:5]
            if ats_result.strengths
            else ["No major strengths identified yet."]
        )

        # ==================================================
        # Improvement Areas
        # ==================================================

        career.improvement_areas = [
            gap.skill
            for gap in skill_gap.high_priority
        ]

        # ==================================================
        # Next Learning Steps
        # ==================================================

        career.next_steps = [
            task.title
            for task in roadmap.tasks[:5]
        ]

        # ==================================================
        # Recommended Projects
        # (Placeholder for v1.0.0)
        # ==================================================

        career.recommended_projects = []

        # ==================================================
        # Recommended Certifications
        # (Placeholder for v1.0.0)
        # ==================================================

        career.recommended_certifications = []

        return career
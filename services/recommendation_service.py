from models.ats_model import ATSResult
from models.recommendation_model import RecommendationResult


class RecommendationService:
    """
    Generates rule-based recommendations from ATS results.

    These recommendations complement the AI-generated
    recommendations and provide immediate feedback based
    on ATS matching.
    """

    def generate(
        self,
        ats_result: ATSResult,
    ) -> RecommendationResult:
        """
        Generate recommendation categories using ATS analysis.
        """

        recommendations = RecommendationResult()

        # =====================================================
        # ATS Optimization
        # =====================================================

        if ats_result.overall_score >= 80:

            recommendations.ats_optimization.append(
                "Excellent ATS compatibility. Continue tailoring your resume for each application."
            )

        elif ats_result.overall_score >= 60:

            recommendations.ats_optimization.extend(
                [
                    "Improve ATS compatibility by adding missing keywords from the job description.",
                    "Match your resume wording with the terminology used in the job posting.",
                ]
            )

        else:

            recommendations.ats_optimization.extend(
                [
                    "Your ATS score is low. Focus on aligning your resume with the required skills.",
                    "Include more relevant keywords from the job description.",
                ]
            )

        # =====================================================
        # Skills to Learn
        # =====================================================

        for skill in ats_result.missing_skills[:5]:

            recommendations.skills_to_learn.append(
                f"Learn {skill} and build at least one project demonstrating it."
            )

        # =====================================================
        # Resume Improvements
        # =====================================================

        recommendations.resume_improvements.extend(
            [
                "Use measurable achievements wherever possible (for example: 'Improved accuracy by 15%').",
                "Tailor your resume for every job application.",
                "Highlight your strongest technical projects near the top of the resume.",
                "Keep formatting clean and ATS-friendly.",
            ]
        )

        # =====================================================
        # Next Steps
        # =====================================================

        if ats_result.overall_score >= 80:

            recommendations.next_steps.extend(
                [
                    "Start preparing for technical interviews.",
                    "Practice behavioral interview questions.",
                    "Continue applying to roles that match your profile.",
                ]
            )

        else:

            recommendations.next_steps.extend(
                [
                    "Complete one additional portfolio project using the missing technologies.",
                    "Update your GitHub repositories with proper documentation.",
                    "Revise your resume after improving your missing skills.",
                ]
            )

        return recommendations

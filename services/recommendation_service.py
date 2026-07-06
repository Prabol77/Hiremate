from models.recommendation_model import RecommendationResult


class RecommendationService:
    """
    Generates intelligent recommendations.
    """

    def generate(
        self,
        ats_result,
    ):

        recommendations = RecommendationResult()

        # ---------------------------------
        # Technical Recommendations
        # ---------------------------------

        for skill in ats_result.missing_skills[:5]:

            recommendations.technical.append(
                f"Learn {skill.title()} and include a project demonstrating it."
            )

        # ---------------------------------
        # Resume Recommendations
        # ---------------------------------

        recommendations.resume.extend(

            [

                "Use measurable achievements (e.g., Improved accuracy by 15%).",

                "Tailor keywords to the job description.",

                "Keep your resume to one page whenever possible.",

                "Prioritize technical projects over coursework."

            ]

        )

        # ---------------------------------
        # Career Recommendations
        # ---------------------------------

        if ats_result.overall_score < 80:

            recommendations.career.extend(

                [

                    "Complete one end-to-end portfolio project.",

                    "Practice interview questions related to missing skills.",

                    "Publish projects on GitHub with proper documentation."

                ]

            )

        else:

            recommendations.career.append(

                "Your profile is strong. Focus on interview preparation."

            )

        return recommendations
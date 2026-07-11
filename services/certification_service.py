"""
Certification Recommendation Service.
"""

from models.certification_model import (
    CertificationRecommendation,
)

from data.certification_library import (
    CERTIFICATION_LIBRARY,
)


class CertificationService:
    """
    Recommend certifications based on
    the candidate's missing skills.
    """

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        ats_result,
    ) -> list[CertificationRecommendation]:
        """
        Generate certification recommendations.
        """

        recommendations = []

        candidate_missing_skills = {

            skill.lower()

            for skill in ats_result.missing_skills

        }

        # ==================================================
        # Certification Matching
        # ==================================================

        for skill, cert in CERTIFICATION_LIBRARY.items():

            if skill not in candidate_missing_skills:

                continue

            recommendations.append(

                CertificationRecommendation(

                    name=cert["name"],

                    provider=cert["provider"],

                    description=cert["description"],

                    difficulty=cert["difficulty"],

                    estimated_duration=cert["duration"],

                    expected_score_gain=cert["gain"],

                    target_companies=cert["companies"],

                    skills_covered=[skill],

                    priority="High",

                )

            )

        return recommendations
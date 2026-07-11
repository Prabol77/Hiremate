"""
Company Match Service.
"""

from models.company_match_model import (
    CompanyMatch,
)

from data.company_profiles import (
    COMPANY_PROFILES,
)


class CompanyMatchService:
    """
    Estimate compatibility between a candidate
    and different companies.
    """

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        resume_data,
        ats_result,
        hireability,
    ) -> list[CompanyMatch]:
        """
        Generate company match scores.
        """

        matches = []

        candidate_skills = {
            skill.lower()
            for skill in resume_data.skills
        }

        # ==================================================
        # Company Matching
        # ==================================================

        for company, profile in COMPANY_PROFILES.items():

            required_skills = [
                skill.lower()
                for skill in profile["skills"]
            ]

            matched = [
                skill
                for skill in required_skills
                if skill in candidate_skills
            ]

            missing = [
                skill
                for skill in required_skills
                if skill not in candidate_skills
            ]

            skill_match = int(

                len(matched)

                / len(required_skills)

                * 100

            )

            overall = int(

                (
                    skill_match * 0.50
                )

                +

                (
                    ats_result.overall_score * 0.25
                )

                +

                (
                    hireability.overall * 0.25
                )

            )

            recommendation = self._recommendation(
                overall,
            )

            matches.append(

                CompanyMatch(

                    company=company,

                    overall_match=overall,

                    skill_match=skill_match,

                    ats_match=int(
                        ats_result.overall_score
                    ),

                    hireability_match=int(
                        hireability.overall
                    ),

                    missing_skills=missing,

                    recommendation=recommendation,

                )

            )

        matches.sort(

            key=lambda company: company.overall_match,

            reverse=True,

        )

        return matches

    # =====================================================
    # Recommendation
    # =====================================================

    def _recommendation(
        self,
        score: int,
    ) -> str:
        """
        Generate recommendation.
        """

        if score >= 90:

            return (
                "Excellent Match"
            )

        if score >= 80:

            return (
                "Strong Match"
            )

        if score >= 70:

            return (
                "Good Match"
            )

        if score >= 60:

            return (
                "Potential Match"
            )

        return (
            "Needs Improvement"
        )
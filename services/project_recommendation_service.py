"""
Project Recommendation Service.
"""

from models.project_recommendation_model import (
    ProjectRecommendation,
)


class ProjectRecommendationService:
    """
    Recommend projects based on
    resume and missing skills.
    """

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        resume_data,
        ats_result,
    ) -> list[ProjectRecommendation]:

        projects = []

        return projects
"""
HireMate Analysis Service.

Coordinates the complete HireMate analysis pipeline.
"""

from services.resume_service import ResumeService
from services.jd_service import JDService
from services.ats_service import ATSService
from services.skill_gap_service import SkillGapService
from services.roadmap_service import RoadmapService
from services.career_intelligence_service import (
    CareerIntelligenceService,
)
from services.ai_service import AIService
from services.recommendation_service import (
    RecommendationService,
)
from services.interview_service import (
    InterviewService,
)


class AnalysisService:
    """
    Central orchestration service for HireMate.

    Pipeline

    Resume
        ↓
    Job Description
        ↓
    ATS Analysis
        ↓
    Skill Gap Analysis
        ↓
    Learning Roadmap
        ↓
    Career Intelligence
        ↓
    AI Review
        ↓
    Recommendations
        ↓
    Interview Questions
        ↓
    Cover Letter
    """

    def __init__(self):

        # ===============================================
        # Resume Intelligence
        # ===============================================

        self.resume_service = ResumeService()

        self.jd_service = JDService()

        self.ats_service = ATSService()

        # ===============================================
        # Career Intelligence
        # ===============================================

        self.skill_gap_service = SkillGapService()

        self.roadmap_service = RoadmapService()

        self.career_intelligence_service = (
            CareerIntelligenceService()
        )

        # ===============================================
        # AI Services
        # ===============================================

        self.ai_service = AIService()

        self.recommendation_service = (
            RecommendationService()
        )

        self.interview_service = (
            InterviewService()
        )

    # ==================================================
    # Main Analysis Pipeline
    # ==================================================

    def analyze(
        self,
        resume_text: str,
        jd_text: str,
    ):

        # ===============================================
        # Resume Parsing
        # ===============================================

        resume_data = self.resume_service.parse(
            resume_text,
        )

        # ===============================================
        # Job Description Parsing
        # ===============================================

        job_data = self.jd_service.parse(
            jd_text,
        )

        # ===============================================
        # ATS Analysis
        # ===============================================

        ats_result = self.ats_service.analyze(
            resume_data,
            job_data.skills,
        )

        # ===============================================
        # Career Intelligence Pipeline
        # ===============================================

        skill_gap = self.skill_gap_service.analyze(
            ats_result,
        )

        roadmap = self.roadmap_service.generate(
            skill_gap,
        )

        career = self.career_intelligence_service.generate(
            resume_data,
            ats_result,
            skill_gap,
            roadmap,
        )

        # ===============================================
        # AI Resume Review
        # ===============================================

        review = self.ai_service.generate_review(
            resume_text,
            jd_text,
        )

        # ===============================================
        # Recommendations
        # ===============================================

        recommendations = (
            self.recommendation_service.generate(
                resume_data,
                ats_result,
            )
        )

        # ===============================================
        # Interview Questions
        # ===============================================

        interview = self.interview_service.generate(
            resume_data,
            jd_text,
        )

        # ===============================================
        # Cover Letter
        # ===============================================

        cover_letter = (
            self.ai_service.generate_cover_letter(
                resume_text,
                jd_text,
            )
        )

        # ===============================================
        # Final Output
        # ===============================================

        return (
            resume_data,
            job_data,
            ats_result,
            skill_gap,
            roadmap,
            career,
            review,
            recommendations,
            interview,
            cover_letter,
        )
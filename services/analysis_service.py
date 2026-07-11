"""
HireMate Analysis Service.

Coordinates the complete HireMate analysis pipeline.
"""
from services.hireability_service import (
    HireabilityService,
)
from services.personalization_service import (
    PersonalizationService,
)
from services.company_match_service import (
    CompanyMatchService,
)
from services.career_coach_service import (
    CareerCoachService,
)
from services.project_recommendation_service import (
    ProjectRecommendationService,
)
from services.certification_service import (
    CertificationService,
)
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
        # ===============================================
        # Hireability Intelligence
        # ===============================================

        self.hireability_service = (
            HireabilityService()
        )

        # ===============================================
        # Project Intelligence
        # ===============================================

        self.project_recommendation_service = (
            ProjectRecommendationService()
        )

        self.career_coach_service = (
            CareerCoachService()
        )
        self.company_match_service = (
            CompanyMatchService()
        )
        self.certification_service = (
            CertificationService()
        )
        self.personalization_service = (
            PersonalizationService()
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

        hireability = self.hireability_service.generate(
            ats_result,
            career,
        )

        # ===============================================
        # Project Recommendations
        # ===============================================

        projects = (
            self.project_recommendation_service.generate(
                resume_data,
                ats_result,
            )
        )

        career_coach = (
            self.career_coach_service.generate(
                resume_data,
                ats_result,
                career,
                hireability,
                projects,
            )
        )

        company_matches = (
            self.company_match_service.generate(
                resume_data,
                ats_result,
                hireability,
            )
        )

        certifications = (
            self.certification_service.generate(
                ats_result,
            )
        )
        personalization = (
            self.personalization_service.generate(
                resume_data,
                career,
                hireability,
                projects,
                company_matches,
                certifications,
            )
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
            hireability,
            projects,
            career_coach,
            company_matches,
            certifications,
            personalization,
            review,
            recommendations,
            interview,
            cover_letter,
        )
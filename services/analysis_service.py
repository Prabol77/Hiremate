from services.ai_service import AIService
from services.ats_service import ATSService
from services.interview_service import InterviewService
from services.jd_service import JDService
from services.resume_service import ResumeService
from services.recommendation_service import RecommendationService

class AnalysisService:
    """
    Main orchestration service for HireMate.

    Coordinates the complete analysis pipeline:
    - Resume Parsing
    - Job Description Parsing
    - ATS Analysis
    - AI Resume Review
    - AI Recommendations
    - AI Interview Questions
    - AI Cover Letter
    """

    def __init__(self):

        self.resume_service = ResumeService()

        self.jd_service = JDService()

        self.ats_service = ATSService()

        self.ai_service = AIService()

        self.interview_service = InterviewService()

        self.recommendation_service = RecommendationService()

    # =====================================================
    # Main Analysis Pipeline
    # =====================================================

    def analyze(
        self,
        resume_text: str,
        jd_text: str,
    ):

        # -------------------------------------------------
        # Parse Resume
        # -------------------------------------------------

        resume_data = self.resume_service.parse(
            resume_text,
        )

        # -------------------------------------------------
        # Parse Job Description
        # -------------------------------------------------

        job_data = self.jd_service.parse(
            jd_text,
        )

        # -------------------------------------------------
        # ATS Analysis
        # -------------------------------------------------

        ats_result = self.ats_service.analyze(
            resume_data,
            job_data.skills,
        )

        # -------------------------------------------------
        # AI Resume Review
        # -------------------------------------------------

        review = self.ai_service.generate_review(
            resume_text,
            jd_text,
        )

        # -------------------------------------------------
        # AI Recommendations
        # -------------------------------------------------

        recommendations = self.recommendation_service.generate(
            resume_data,
            ats_result,
        )

        # -------------------------------------------------
        # AI Interview Questions
        # (Uses structured ResumeData)
        # -------------------------------------------------

        interview = self.interview_service.generate(
            resume_data,
            jd_text,
        )

        # -------------------------------------------------
        # AI Cover Letter
        # -------------------------------------------------

        cover_letter = self.ai_service.generate_cover_letter(
            resume_text,
            jd_text,
        )

        # -------------------------------------------------
        # Return Complete Analysis
        # -------------------------------------------------

        return (
            resume_data,
            job_data,
            ats_result,
            review,
            recommendations,
            interview,
            cover_letter,
        )
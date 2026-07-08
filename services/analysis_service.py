from services.ai_service import AIService
from services.ats_service import ATSService
from services.interview_service import InterviewService
from services.jd_service import JDService
from services.resume_service import ResumeService


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
    """

    def __init__(self):
        """
        Initialize all analysis services.
        """

        self.resume_service = ResumeService()

        self.jd_service = JDService()

        self.ats_service = ATSService()

        self.ai_service = AIService()

        self.interview_service = InterviewService()

    def analyze(
            
        self,
        resume_text: str,
        jd_text: str,
    ):
        """
        Execute the complete HireMate analysis pipeline.
        """

    # ==========================================
    # Resume Parsing
    # ==========================================

        resume_data = self.resume_service.parse(
            resume_text,
        )

    # ==========================================
    # Job Description Parsing
    # ==========================================

        job_data = self.jd_service.parse(
            jd_text,
        )

    # ==========================================
    # ATS Matching
    # ==========================================

        ats_result = self.ats_service.compare(
            resume_data,
            job_data,
        )

    # ==========================================
    # AI Resume Review
    # ==========================================

        review = self.ai_service.generate_review(
            resume_text,
            jd_text,
        )

    # ==========================================
    # AI Recommendations
    # ==========================================

        recommendations = self.ai_service.generate_recommendations(
            resume_text,
            jd_text,
        )

    # ==========================================
    # AI Interview Questions
    # ==========================================

        interview = self.interview_service.generate(
            resume_text,
            jd_text,
        )

    # ==========================================
    # AI Cover Letter
    # ==========================================

        cover_letter = self.ai_service.generate_cover_letter(
            resume_text,
            jd_text,
        )

    # ==========================================
    # Return Complete Analysis
    # ==========================================

        return (
            resume_data,
            job_data,
            ats_result,
            review,
            recommendations,
            interview,
            cover_letter,
        )
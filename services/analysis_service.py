from services.resume_service import ResumeService
from services.jd_service import JDService
from services.ats_service import ATSService
from services.ai_service import AIService
from services.recommendation_service import RecommendationService
from services.interview_service import InterviewService


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

        self.recommendation_service = RecommendationService()

        self.interview_service = InterviewService()

    def analyze(
        self,
        resume_text: str,
        jd_text: str,
    ):
        """
        Execute the complete HireMate analysis pipeline.

        Args:
            resume_text (str):
                Extracted resume text.

            jd_text (str):
                Extracted job description text.

        Returns:
            tuple:
            (
                ResumeData,
                JobData,
                ATSResult,
                ReviewResult,
                RecommendationResult,
                InterviewResult,
            )
        """

        # ==========================================
        # Resume Parsing
        # ==========================================

        resume_data = self.resume_service.parse(
            resume_text
        )

        # ==========================================
        # Job Description Parsing
        # ==========================================

        job_data = self.jd_service.parse(
            jd_text
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

        recommendations = (
            self.recommendation_service.generate(
                ats_result
            )
        )

        # ==========================================
        # AI Interview Questions
        # ==========================================

        interview = (
            self.interview_service.generate(
                resume_text,
                jd_text,
            )
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
        )
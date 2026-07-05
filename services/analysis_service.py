from services.resume_service import ResumeService
from services.jd_service import JDService
from services.ats_service import ATSService


class AnalysisService:
    """
    Main orchestration service.

    Coordinates:
    - Resume Parsing
    - Job Description Parsing
    - ATS Comparison
    """

    def __init__(self):
        self.resume_service = ResumeService()
        self.jd_service = JDService()
        self.ats_service = ATSService()

    def analyze(self, resume_text: str, jd_text: str):
        """
        Analyze a resume against a job description.

        Args:
            resume_text (str): Extracted resume text.
            jd_text (str): Extracted job description text.

        Returns:
            tuple:
                ResumeData,
                JobData,
                ATSResult
        """

        resume_data = self.resume_service.parse(resume_text)

        job_data = self.jd_service.parse(jd_text)

        ats_result = self.ats_service.compare(
            resume_data,
            job_data,
        )

        return (
            resume_data,
            job_data,
            ats_result,
        )
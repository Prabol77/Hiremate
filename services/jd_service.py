import re

from models.job_model import JobData
from services.skill_service import SkillService


class JDService:
    """
    Service responsible for extracting structured information
    from a Job Description.
    """

    def __init__(self):
        self.job = JobData()
        self.skill_service = SkillService()

    def extract_job_title(self, text: str) -> None:
        """
        Extract the job title.
        Assumption: First non-empty line is the title.
        """

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if lines:
            self.job.job_info.title = lines[0]

    def extract_experience(self, text: str) -> None:
        """
        Extract required experience.
        """

        pattern = (
            r"(\d+\+?\s*(?:-|to)?\s*\d*\+?\s*"
            r"(?:years|year|yrs|yr))"
        )

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            self.job.requirements.experience = match.group()

    def extract_skills(self, text: str) -> None:
        """
        Extract required technical skills.
        """

        self.job.skills = self.skill_service.extract_skills(text)

    def parse(self, text: str) -> JobData:
        """
        Parse Job Description text.
        """

        self.extract_job_title(text)
        self.extract_experience(text)
        self.extract_skills(text)

        return self.job
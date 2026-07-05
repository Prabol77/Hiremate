import re

from models.resume_model import ResumeData
from services.skill_service import SkillService


class ResumeService:
    """
    Service responsible for extracting structured information
    from resume text.
    """

    def __init__(self):
        self.resume = ResumeData()
        self.skill_service = SkillService()

    def extract_name(self, text: str) -> None:
        """
        Extract candidate name.
        """

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if lines:
            self.resume.personal_info.name = lines[0]

    def extract_email(self, text: str) -> None:
        """
        Extract email address.
        """

        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(email_pattern, text)

        if match:
            self.resume.personal_info.email = match.group()

    def extract_phone(self, text: str) -> None:
        """
        Extract phone number.
        """

        phone_pattern = r"(\+?\d[\d\s\-]{8,}\d)"

        match = re.search(phone_pattern, text)

        if match:
            self.resume.personal_info.phone = match.group()

    def extract_skills(self, text: str) -> None:
        """
        Extract technical skills using SkillService.
        """

        self.resume.skills = self.skill_service.extract_skills(text)

    def parse(self, text: str) -> ResumeData:
        """
        Parse resume text and return structured ResumeData.
        """

        self.extract_name(text)
        self.extract_email(text)
        self.extract_phone(text)
        self.extract_skills(text)

        return self.resume
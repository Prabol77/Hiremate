import re

from models.resume_model import ResumeData
from services.skill_service import SkillService


class ResumeService:
    """
    Service responsible for parsing resume text into structured data.
    """

    def __init__(self):

        self.resume = ResumeData()

        self.skill_service = SkillService()

    def extract_name(self, text: str):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if lines:

            self.resume.personal_info.name = lines[0]

    def extract_email(self, text: str):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        if match:

            self.resume.personal_info.email = match.group()

    def extract_phone(self, text: str):

        pattern = r"(\+?\d[\d\s\-]{8,}\d)"

        match = re.search(pattern, text)

        if match:

            self.resume.personal_info.phone = match.group()

    def parse(self, text: str):

        self.resume = ResumeData()

        self.extract_name(text)

        self.extract_email(text)

        self.extract_phone(text)

        self.resume.skills = (
            self.skill_service.extract_skills(text)
        )

        return self.resume
import re

from models.resume_model import ResumeData
from services.skill_service import SkillService


class ResumeService:
    """
    Service responsible for parsing resume text into structured data.
    """

    SECTION_HEADERS = {
        "summary": [
            "summary",
            "professional summary",
            "profile",
            "objective",
            "about",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core skills",
        ],
        "projects": [
            "projects",
            "academic projects",
            "personal projects",
        ],
        "experience": [
            "experience",
            "work experience",
            "employment",
            "internship",
        ],
        "education": [
            "education",
            "academic background",
            "qualification",
        ],
        "certifications": [
            "certifications",
            "certificates",
            "licenses",
        ],
        "achievements": [
            "achievements",
            "awards",
            "accomplishments",
        ],
        "languages": [
            "languages",
        ],
    }

    def __init__(self):

        self.resume = ResumeData()

        self.skill_service = SkillService()

    # =====================================================
    # Personal Information
    # =====================================================

    def extract_name(
        self,
        text: str,
    ):
        """
        Attempt to identify the candidate's name.

        Usually the name appears within the first few
        non-empty lines and does not contain numbers,
        email addresses, URLs or phone numbers.
        """

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        ignored_keywords = {
            "resume",
            "curriculum vitae",
            "cv",
        }

        for line in lines[:5]:

            lowered = line.lower()

            if lowered in ignored_keywords:
                continue

            if "@" in line:
                continue

            if re.search(r"\d", line):
                continue

            if "http" in lowered:
                continue

            if "linkedin" in lowered:
                continue

            if "github" in lowered:
                continue

            self.resume.personal_info.name = line

            break

    def extract_email(
        self,
        text: str,
    ):

        pattern = r"[A-Za-z0-9._%+-]+" r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(
            pattern,
            text,
        )

        if match:

            self.resume.personal_info.email = match.group()

    def extract_phone(
        self,
        text: str,
    ):

        pattern = r"(\+?\d[\d\s\-]{8,}\d)"

        match = re.search(
            pattern,
            text,
        )

        if match:

            self.resume.personal_info.phone = match.group()

    # =====================================================
    # Resume Sections
    # =====================================================

    def extract_sections(
        self,
        text: str,
    ):
        """
        Extract resume sections using common headings.

        Stores the raw text of every detected section.
        """

        current_section = "general"

        self.resume.sections.setdefault(
            current_section,
            "",
        )

        for line in text.splitlines():

            cleaned = line.strip()

            if not cleaned:
                continue

            normalized = re.sub(
                r"[^a-z ]",
                "",
                cleaned.lower(),
            ).strip()

            found_section = False

            for (
                section,
                aliases,
            ) in self.SECTION_HEADERS.items():

                if any(alias in normalized for alias in aliases):

                    current_section = section

                    self.resume.sections.setdefault(
                        current_section,
                        "",
                    )

                    found_section = True

                    break

            if found_section:
                continue

            self.resume.sections[current_section] += cleaned + "\n"

    # =====================================================
    # Main Parser
    # =====================================================

    def parse(
        self,
        text: str,
    ) -> ResumeData:
        """
        Parse resume text into structured ResumeData.
        """

        self.resume = ResumeData()

        self.extract_name(text)

        self.extract_email(text)

        self.extract_phone(text)

        self.extract_sections(text)

        self.resume.skills = self.skill_service.extract_skills(text)

        return self.resume

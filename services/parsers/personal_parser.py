"""
Personal Information Parser.
"""

import re

from models.resume_model import ResumeData


class PersonalParser:
    """
    Extract personal information from resume text.
    """

    def parse(
        self,
        text: str,
        resume: ResumeData,
    ):
        """
        Parse all personal information.
        """

        self.extract_name(
            text,
            resume,
        )

        self.extract_email(
            text,
            resume,
        )

        self.extract_phone(
            text,
            resume,
        )

        self.extract_linkedin(
            text,
            resume,
        )

        self.extract_github(
            text,
            resume,
        )

        self.extract_location(
            text,
            resume,
        )

    # =====================================================
    # Name
    # =====================================================

    def extract_name(
        self,
        text,
        resume,
    ):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        ignored = {

            "resume",

            "curriculum vitae",

            "cv",

        }

        for line in lines[:6]:

            lower = line.lower()

            if lower in ignored:
                continue

            if "@" in line:
                continue

            if re.search(r"\d", line):
                continue

            if "linkedin" in lower:
                continue

            if "github" in lower:
                continue

            if "http" in lower:
                continue

            resume.personal_info.name = line

            return

    # =====================================================
    # Email
    # =====================================================

    def extract_email(
        self,
        text,
        resume,
    ):

        match = re.search(

            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

            text,

        )

        if match:

            resume.personal_info.email = match.group()

    # =====================================================
    # Phone
    # =====================================================

    def extract_phone(
        self,
        text,
        resume,
    ):

        match = re.search(

            r"(\+?\d[\d\s\-]{8,}\d)",

            text,

        )

        if match:

            resume.personal_info.phone = match.group()

    # =====================================================
    # LinkedIn
    # =====================================================

    def extract_linkedin(
        self,
        text,
        resume,
    ):

        match = re.search(

            r"(https?://)?(www\.)?linkedin\.com/[^\s]+",

            text,

            re.IGNORECASE,

        )

        if match:

            resume.personal_info.linkedin = match.group()

    # =====================================================
    # GitHub
    # =====================================================

    def extract_github(
        self,
        text,
        resume,
    ):

        match = re.search(

            r"(https?://)?(www\.)?github\.com/[^\s]+",

            text,

            re.IGNORECASE,

        )

        if match:

            resume.personal_info.github = match.group()

    # =====================================================
    # Location
    # =====================================================

    def extract_location(
        self,
        text,
        resume,
    ):

        lines = text.splitlines()

        for line in lines[:15]:

            line = line.strip()

            if not line:

                continue

            if "," in line:

                if any(

                    char.isdigit()

                    for char in line

                ):

                    continue

                if len(line.split()) <= 6:

                    resume.personal_info.location = line

                    return
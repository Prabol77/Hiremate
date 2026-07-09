"""
Resume Section Parser.
"""

import re

from services.parsers.base_parser import BaseParser


class SectionParser(BaseParser):
    """
    Detect and split resume into sections.
    """

    SECTION_HEADERS = {
        "summary": [
            "summary",
            "professional summary",
            "objective",
            "profile",
            "about",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core skills",
        ],
        "education": [
            "education",
            "academic background",
            "qualification",
        ],
        "experience": [
            "experience",
            "work experience",
            "employment",
            "internship",
        ],
        "projects": [
            "projects",
            "academic projects",
            "personal projects",
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

    def parse(
        self,
        text,
        resume,
    ):
        """
        Split resume into logical sections.
        """

        resume.sections = {}

        current_section = "general"

        resume.sections[current_section] = ""

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            normalized = re.sub(
                r"[^a-z ]",
                "",
                line.lower(),
            ).strip()

            found = False

            for section, aliases in self.SECTION_HEADERS.items():

                if normalized in aliases:

                    current_section = section

                    resume.sections.setdefault(
                        current_section,
                        "",
                    )

                    found = True

                    break

            if found:
                continue

            resume.sections[current_section] += (
                line + "\n"
            )
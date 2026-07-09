"""
Education Parser.
"""

from models.resume_model import Education


class EducationParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "education",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if not line:
                continue

            resume.education.append(
                Education(
                    degree=line,
                )
            )
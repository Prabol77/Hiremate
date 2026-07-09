"""
Experience Parser.
"""

from models.resume_model import Experience


class ExperienceParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "experience",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if not line:
                continue

            resume.experience.append(
                Experience(
                    company=line,
                )
            )
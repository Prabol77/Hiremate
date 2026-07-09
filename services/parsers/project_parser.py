"""
Project Parser.
"""

from models.resume_model import Project


class ProjectParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "projects",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if not line:
                continue

            resume.projects.append(
                Project(
                    title=line,
                )
            )
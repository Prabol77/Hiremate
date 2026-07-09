"""
Achievement Parser.
"""


class AchievementParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "achievements",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if line:

                resume.achievements.append(
                    line,
                )
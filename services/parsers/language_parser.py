"""
Language Parser.
"""


class LanguageParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "languages",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if line:

                resume.languages.append(
                    line,
                )
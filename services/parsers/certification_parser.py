"""
Certification Parser.
"""


class CertificationParser:

    def parse(
        self,
        resume,
    ):

        section = resume.sections.get(
            "certifications",
            "",
        )

        if not section:
            return

        for line in section.splitlines():

            line = line.strip()

            if line:

                resume.certifications.append(
                    line,
                )
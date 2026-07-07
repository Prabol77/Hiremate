from dataclasses import dataclass


@dataclass
class CoverLetterResult:
    """
    Stores the AI-generated cover letter.
    """

    company_name: str = ""

    position: str = ""

    greeting: str = ""

    introduction: str = ""

    body: str = ""

    conclusion: str = ""

    closing: str = ""

    full_letter: str = ""
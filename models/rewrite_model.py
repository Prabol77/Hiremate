from dataclasses import dataclass


@dataclass
class RewriteResult:
    """
    Represents the AI rewrite of a single resume section.
    """

    section_name: str = ""

    original_text: str = ""

    improved_text: str = ""

    explanation: str = ""

    estimated_improvement: str = ""
from dataclasses import dataclass


@dataclass
class RewriteResult:
    """
    Stores AI-generated resume rewrite.
    """

    original_text: str = ""

    improved_text: str = ""

    explanation: str = ""

    estimated_improvement: str = ""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ReviewResult:
    """
    Stores AI-generated resume review.
    """

    summary: str = ""

    strengths: List[str] = field(default_factory=list)

    weaknesses: List[str] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)

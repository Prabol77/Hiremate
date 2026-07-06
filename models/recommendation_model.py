from dataclasses import dataclass, field
from typing import List


@dataclass
class RecommendationResult:
    """
    Stores AI recommendations.
    """

    technical: List[str] = field(default_factory=list)

    resume: List[str] = field(default_factory=list)

    career: List[str] = field(default_factory=list)
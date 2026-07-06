from dataclasses import dataclass, field
from typing import List


@dataclass
class ATSResult:
    """
    Stores ATS matching results.
    """

    overall_score: float = 0.0

    matched_skills: List[str] = field(default_factory=list)

    missing_skills: List[str] = field(default_factory=list)

    additional_skills: List[str] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)

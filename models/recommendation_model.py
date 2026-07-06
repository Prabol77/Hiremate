from dataclasses import dataclass, field
from typing import List


@dataclass
class RecommendationResult:
    """
    Stores AI-generated career recommendations.
    """

    ats_optimization: List[str] = field(default_factory=list)

    skills_to_learn: List[str] = field(default_factory=list)

    resume_improvements: List[str] = field(default_factory=list)

    next_steps: List[str] = field(default_factory=list)

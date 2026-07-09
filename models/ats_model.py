from dataclasses import dataclass, field

from typing import List


@dataclass
class ATSResult:
    """
    Stores ATS evaluation results.
    """

    overall_score: float = 0.0

    # Individual scores

    skills_score: float = 0.0

    experience_score: float = 0.0

    projects_score: float = 0.0

    education_score: float = 0.0

    completeness_score: float = 0.0

    # Skills

    matched_skills: List[str] = field(
        default_factory=list
    )

    missing_skills: List[str] = field(
        default_factory=list
    )

    # AI Explanation

    strengths: List[str] = field(
        default_factory=list
    )

    weaknesses: List[str] = field(
        default_factory=list
    )

    recommendations: List[str] = field(
        default_factory=list
    )
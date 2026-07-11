from dataclasses import dataclass, field


@dataclass
class ProjectRecommendation:
    """
    Represents a portfolio project recommendation.
    """

    title: str = ""

    description: str = ""

    technologies: list[str] = field(
        default_factory=list
    )

    skills_covered: list[str] = field(
        default_factory=list
    )

    difficulty: str = ""

    estimated_duration: str = ""

    expected_score_gain: int = 0

    priority: str = ""
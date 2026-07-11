from dataclasses import dataclass, field


@dataclass
class CertificationRecommendation:
    """
    Represents a certification recommendation.
    """

    name: str = ""

    provider: str = ""

    description: str = ""

    difficulty: str = ""

    estimated_duration: str = ""

    expected_score_gain: int = 0

    target_companies: list[str] = field(
        default_factory=list
    )

    skills_covered: list[str] = field(
        default_factory=list
    )

    priority: str = ""
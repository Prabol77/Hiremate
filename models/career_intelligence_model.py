from dataclasses import dataclass, field


@dataclass
class CareerIntelligence:
    """
    Unified career intelligence generated
    from resume analysis.
    """

    readiness_score: int = 0

    stage: str = ""

    confidence: str = ""

    estimated_duration: str = ""

    summary: str = ""

    strengths: list[str] = field(
        default_factory=list
    )

    improvement_areas: list[str] = field(
        default_factory=list
    )

    next_steps: list[str] = field(
        default_factory=list
    )

    recommended_projects: list[str] = field(
        default_factory=list
    )

    recommended_certifications: list[str] = field(
        default_factory=list
    )
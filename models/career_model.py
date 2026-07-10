from dataclasses import dataclass, field


@dataclass
class CareerGoal:

    current_level: str = ""

    target_role: str = ""

    readiness_score: int = 0

    estimated_duration: str = ""

    strengths: list[str] = field(
        default_factory=list
    )

    focus_areas: list[str] = field(
        default_factory=list
    )
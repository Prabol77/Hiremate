from dataclasses import dataclass, field


@dataclass
class CareerCoachResult:
    """
    AI-generated personalized career coaching.
    """

    summary: str = ""

    strengths: list[str] = field(
        default_factory=list
    )

    focus_areas: list[str] = field(
        default_factory=list
    )

    weekly_goals: list[str] = field(
        default_factory=list
    )

    recommended_projects: list[str] = field(
        default_factory=list
    )

    recommended_certifications: list[str] = field(
        default_factory=list
    )

    interview_strategy: list[str] = field(
        default_factory=list
    )

    final_message: str = ""
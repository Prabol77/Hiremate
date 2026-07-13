from dataclasses import dataclass, field


@dataclass
class HireabilityScore:
    """
    Overall HireMate employability score.
    """

    overall: int = 0

    resume: int = 0

    ats: int = 0

    technical: int = 0

    projects: int = 0

    career: int = 0

    interview: int = 0

    grade: str = ""

    improvement_potential: int = 0

    # ==================================================
    # New v1.0.0 Fields
    # ==================================================

    strengths: list[str] = field(
        default_factory=list
    )

    weaknesses: list[str] = field(
        default_factory=list
    )

    next_actions: list[str] = field(
        default_factory=list
    )
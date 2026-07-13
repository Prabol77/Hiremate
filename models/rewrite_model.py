from dataclasses import dataclass, field


@dataclass
class RewriteResult:
    """
    AI rewritten resume.
    """

    professional_summary: str = ""

    experience: str = ""

    projects: str = ""

    skills: str = ""

    suggestions: list[str] = field(
        default_factory=list,
    )

    ats_improvement: str = ""
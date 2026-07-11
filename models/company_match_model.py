from dataclasses import dataclass, field


@dataclass
class CompanyMatch:

    company: str = ""

    overall_match: int = 0

    skill_match: int = 0

    ats_match: int = 0

    hireability_match: int = 0

    missing_skills: list[str] = field(
        default_factory=list
    )

    recommendation: str = ""
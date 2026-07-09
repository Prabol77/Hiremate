from dataclasses import dataclass, field


@dataclass
class RecommendationResult:

    technical: list[str] = field(
        default_factory=list
    )

    resume: list[str] = field(
        default_factory=list
    )

    career: list[str] = field(
        default_factory=list
    )
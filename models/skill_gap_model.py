from dataclasses import dataclass, field


@dataclass
class SkillGap:

    skill: str

    priority: str

    importance: int

    reason: str = ""


@dataclass
class SkillGapResult:

    overall_score: int = 0

    high_priority: list[SkillGap] = field(
        default_factory=list
    )

    medium_priority: list[SkillGap] = field(
        default_factory=list
    )

    low_priority: list[SkillGap] = field(
        default_factory=list
    )
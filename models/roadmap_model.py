from dataclasses import dataclass, field


@dataclass
class LearningTask:

    week: int

    title: str

    description: str

    estimated_hours: int = 8


@dataclass
class LearningRoadmap:

    duration_weeks: int = 4

    tasks: list[LearningTask] = field(
        default_factory=list
    )
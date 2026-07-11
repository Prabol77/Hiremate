from dataclasses import dataclass, field


@dataclass
class SimulationAction:
    """
    Represents a simulated improvement.
    """

    title: str = ""

    description: str = ""

    score_gain: int = 0

    estimated_score: int = 0

    difficulty: str = ""


@dataclass
class ScoreSimulation:
    """
    Complete Hireability simulation.
    """

    current_score: int = 0

    actions: list[SimulationAction] = field(
        default_factory=list
    )
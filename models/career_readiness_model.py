from dataclasses import dataclass


@dataclass
class CareerReadiness:

    score: int = 0

    stage: str = ""

    confidence: str = ""

    summary: str = ""

    estimated_duration: str = ""
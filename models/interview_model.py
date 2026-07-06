from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class InterviewResult:
    """
    Stores AI-generated interview questions.
    """

    questions: Dict[str, List[str]] = field(default_factory=dict)

    overall_tips: List[str] = field(default_factory=list)

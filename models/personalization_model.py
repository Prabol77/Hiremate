from dataclasses import dataclass


@dataclass
class PersonalizationResult:

    career_summary: str = ""

    why_projects: str = ""

    why_certifications: str = ""

    why_companies: str = ""

    final_advice: str = ""
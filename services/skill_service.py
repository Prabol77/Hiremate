import re
from typing import List

import pandas as pd


class SkillService:
    """
    Extract technical skills from resume text.
    """

    def __init__(self, csv_path: str = "data/skills.csv"):

        try:
            skills = pd.read_csv(csv_path)

            self.skill_list = (
                skills["skill"]
                .dropna()
                .astype(str)
                .str.lower()
                .tolist()
            )

        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"Skills database not found: {csv_path}"
            ) from exc

    def extract_skills(self, text: str) -> List[str]:
        """
        Extract technical skills from resume text.
        """

        text = text.lower()

        detected = []

        for skill in self.skill_list:

            pattern = rf"\b{re.escape(skill)}\b"

            if re.search(pattern, text):
                detected.append(skill.title())

        return sorted(set(detected))
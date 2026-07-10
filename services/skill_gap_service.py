from models.skill_gap_model import (
    SkillGap,
    SkillGapResult,
)


class SkillGapService:
    """
    Analyze missing skills and prioritize them.
    """

    HIGH_PRIORITY = {
        "docker",
        "aws",
        "azure",
        "gcp",
        "kubernetes",
        "terraform",
        "react",
        "node.js",
        "python",
        "java",
        "sql",
        "mongodb",
    }

    MEDIUM_PRIORITY = {
        "redis",
        "jenkins",
        "git",
        "linux",
        "fastapi",
        "flask",
        "django",
        "postgresql",
        "mysql",
    }

    def analyze(
        self,
        ats_result,
    ) -> SkillGapResult:

        result = SkillGapResult()

        missing = ats_result.missing_skills

        matched = ats_result.matched_skills

        total = len(matched) + len(missing)

        if total:

            result.overall_score = round(
                len(matched) / total * 100
            )

        else:

            result.overall_score = 100

        for skill in missing:

            name = skill.lower()

            if name in self.HIGH_PRIORITY:

                result.high_priority.append(

                    SkillGap(
                        skill=skill,
                        priority="High",
                        importance=3,
                        reason="Frequently required for modern software roles.",
                    )
                )

            elif name in self.MEDIUM_PRIORITY:

                result.medium_priority.append(

                    SkillGap(
                        skill=skill,
                        priority="Medium",
                        importance=2,
                        reason="Helpful for improving employability.",
                    )
                )

            else:

                result.low_priority.append(

                    SkillGap(
                        skill=skill,
                        priority="Low",
                        importance=1,
                        reason="Nice-to-have skill.",
                    )
                )

        return result
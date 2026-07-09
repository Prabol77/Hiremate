from models.ats_model import ATSResult


class ATSService:
    """
    Intelligent ATS scoring service.
    """

    # -----------------------------------------------------
    # Public API
    # -----------------------------------------------------

    def analyze(
        self,
        resume_data,
        jd_skills,
    ) -> ATSResult:

        result = ATSResult()

        result.skills_score = self.calculate_skill_score(
            resume_data,
            jd_skills,
            result,
        )

        result.projects_score = self.calculate_project_score(
            resume_data,
        )

        result.experience_score = self.calculate_experience_score(
            resume_data,
        )

        result.education_score = self.calculate_education_score(
            resume_data,
        )

        result.completeness_score = self.calculate_completeness_score(
            resume_data,
        )

        result.overall_score = self.calculate_overall_score(
            result,
        )

        self.generate_feedback(
            result,
        )

        return result

    # -----------------------------------------------------
    # Skills
    # -----------------------------------------------------

    def calculate_skill_score(
        self,
        resume_data,
        jd_skills,
        result,
    ):

        resume_skills = {

            skill.lower()

            for skill in resume_data.skills

        }

        jd = {

            skill.lower()

            for skill in jd_skills

        }

        matched = sorted(
            resume_skills & jd
        )

        missing = sorted(
            jd - resume_skills
        )

        result.matched_skills = matched
        result.missing_skills = missing

        if not jd:

            return 100

        return len(matched) / len(jd) * 100

    # -----------------------------------------------------
    # Projects
    # -----------------------------------------------------

    def calculate_project_score(
        self,
        resume_data,
    ):

        projects = len(
            resume_data.projects
        )

        return min(
            projects * 25,
            100,
        )

    # -----------------------------------------------------
    # Experience
    # -----------------------------------------------------

    def calculate_experience_score(
        self,
        resume_data,
    ):

        experience = len(
            resume_data.experience
        )

        return min(
            experience * 30,
            100,
        )

    # -----------------------------------------------------
    # Education
    # -----------------------------------------------------

    def calculate_education_score(
        self,
        resume_data,
    ):

        if resume_data.education:

            return 100

        return 0

    # -----------------------------------------------------
    # Completeness
    # -----------------------------------------------------

    def calculate_completeness_score(
        self,
        resume_data,
    ):

        fields = [

            resume_data.personal_info.name,

            resume_data.personal_info.email,

            resume_data.personal_info.phone,

            resume_data.skills,

            resume_data.education,

            resume_data.projects,

            resume_data.experience,

            resume_data.certifications,

        ]

        completed = 0

        for field in fields:

            if isinstance(
                field,
                list,
            ):

                if field:

                    completed += 1

            elif field:

                completed += 1

        return (
            completed / len(fields)
        ) * 100

    # -----------------------------------------------------
    # Overall
    # -----------------------------------------------------

    def calculate_overall_score(
        self,
        result,
    ):

        return round(

            result.skills_score * 0.40 +

            result.projects_score * 0.20 +

            result.experience_score * 0.20 +

            result.education_score * 0.10 +

            result.completeness_score * 0.10,

            1,

        )

    # -----------------------------------------------------
    # Feedback
    # -----------------------------------------------------

    def generate_feedback(
        self,
        result,
    ):

        if result.skills_score >= 80:

            result.strengths.append(
                "Excellent skill match with the job description."
            )

        elif result.skills_score >= 60:

            result.strengths.append(
                "Good technical skill coverage."
            )

        else:

            result.weaknesses.append(
                "Skill match is below the desired level."
            )

        if result.projects_score >= 75:

            result.strengths.append(
                "Strong project portfolio."
            )

        else:

            result.weaknesses.append(
                "Add more relevant projects."
            )

        if result.experience_score < 50:

            result.weaknesses.append(
                "Professional experience is limited."
            )

        if result.missing_skills:

            result.recommendations.append(

                "Consider learning: "

                + ", ".join(
                    result.missing_skills[:5]
                )

            )
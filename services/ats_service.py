from models.ats_model import ATSResult
from models.job_model import JobData
from models.resume_model import ResumeData


class ATSService:
    """
    Compare a parsed resume against a parsed job description
    and generate ATS matching results.
    """

    def compare(
        self,
        resume: ResumeData,
        job: JobData,
    ) -> ATSResult:
        """
        Compare resume skills with job skills.

        Returns:
            ATSResult
        """

        result = ATSResult()

        resume_skills = {
            skill.strip().lower() for skill in resume.skills if skill.strip()
        }

        job_skills = {skill.strip().lower() for skill in job.skills if skill.strip()}

        matched = sorted(resume_skills & job_skills)

        missing = sorted(job_skills - resume_skills)

        additional = sorted(resume_skills - job_skills)

        result.matched_skills = [skill.title() for skill in matched]

        result.missing_skills = [skill.title() for skill in missing]

        result.additional_skills = [skill.title() for skill in additional]

        if job_skills:

            result.overall_score = round(
                (len(matched) / len(job_skills)) * 100,
                2,
            )

        else:

            result.overall_score = 0.0

        # ==========================================
        # Basic Recommendations
        # ==========================================

        if result.overall_score >= 80:

            result.recommendations.append(
                "Excellent ATS match. Your resume aligns well with the job description."
            )

        elif result.overall_score >= 60:

            result.recommendations.append(
                "Good ATS match. Consider adding the missing skills to improve your score."
            )

        else:

            result.recommendations.append(
                "Low ATS match. Focus on acquiring and highlighting the missing skills."
            )

        if missing:

            result.recommendations.append(
                f"Add {len(missing)} missing skill(s) mentioned in the job description."
            )

        if additional:

            result.recommendations.append(
                "Keep your additional skills—they strengthen your overall profile."
            )

        return result

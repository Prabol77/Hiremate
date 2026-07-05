from models.ats_model import ATSResult
from models.job_model import JobData
from models.resume_model import ResumeData


class ATSService:
    """
    Compare ResumeData with JobData.
    """

    def compare(
        self,
        resume: ResumeData,
        job: JobData,
    ) -> ATSResult:

        result = ATSResult()

        resume_skills = {
            skill.lower()
            for skill in resume.skills
        }

        job_skills = {
            skill.lower()
            for skill in job.skills
        }

        matched = resume_skills & job_skills

        missing = job_skills - resume_skills

        additional = resume_skills - job_skills

        result.matched_skills = sorted(matched)

        result.missing_skills = sorted(missing)

        result.additional_skills = sorted(additional)

        if job_skills:

            result.overall_score = round(
                (len(matched) / len(job_skills)) * 100,
                2,
            )

        return result
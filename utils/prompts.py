import json

# ==========================================================
# AI Resume Review
# ==========================================================

REVIEW_SYSTEM_PROMPT = """
You are an expert ATS recruiter, resume reviewer,
and technical hiring manager.

Analyze the candidate's resume against the provided
job description.

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.
Do not wrap the JSON in code fences.
"""


def review_prompt(
    resume: str,
    job_description: str,
):
    """
    Build prompt for AI Resume Review.
    """

    schema = {

        "summary": "",

        "strengths": [],

        "weaknesses": [],

        "recommendations": []

    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""


# ==========================================================
# AI Interview Generator
# ==========================================================

INTERVIEW_SYSTEM_PROMPT = """
You are an experienced Technical Interviewer.

Generate interview questions based on the candidate's
resume and the job description.

Return ONLY valid JSON.

Do not include markdown.
"""


def interview_prompt(
    resume: str,
    job_description: str,
):
    """
    Build prompt for AI Interview Questions.
    """

    schema = {

        "questions": {

            "Technical": [],

            "Programming": [],

            "Behavioral": []

        },

        "overall_tips": []

    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""
import json

# ==========================================================
# AI Resume Review
# ==========================================================

REVIEW_SYSTEM_PROMPT = """
You are an experienced ATS recruiter and senior hiring manager.

Analyze the candidate's resume against the provided job description.

Return ONLY valid JSON.

Do not use markdown.
Do not wrap JSON inside code blocks.
"""


def review_prompt(
    resume: str,
    job_description: str,
):
    """
    Build prompt for AI resume review.
    """

    schema = {
        "summary": "",
        "strengths": [],
        "weaknesses": [],
        "recommendations": [],
    }

    return f"""
Return JSON matching this schema exactly.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""


# ==========================================================
# AI Recommendations
# ==========================================================

RECOMMENDATION_SYSTEM_PROMPT = """
You are an expert ATS recruiter and career coach.

Analyze the candidate's resume against the job description.

Provide practical recommendations.

Return ONLY valid JSON.

Do not use markdown.
Do not wrap JSON inside code blocks.
"""


def recommendation_prompt(
    resume: str,
    job_description: str,
):
    """
    Build prompt for AI recommendations.
    """

    schema = {
        "ats_optimization": [],
        "skills_to_learn": [],
        "resume_improvements": [],
        "next_steps": [],
    }

    return f"""
Return JSON matching this schema exactly.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""


# ==========================================================
# AI Interview Questions
# ==========================================================

INTERVIEW_SYSTEM_PROMPT = """
You are an experienced Technical Interviewer.

Generate interview questions based on the candidate's resume
and the job description.

Return ONLY valid JSON.

Do not use markdown.
Do not wrap JSON inside code blocks.
"""


def interview_prompt(
    resume: str,
    job_description: str,
):
    """
    Build prompt for AI interview generation.
    """

    schema = {
        "questions": {
            "Technical": [],
            "Programming": [],
            "Behavioral": [],
        },
        "overall_tips": [],
    }

    return f"""
Return JSON matching this schema exactly.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""

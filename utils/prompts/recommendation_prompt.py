import json

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
    schema = {
        "ats_optimization": [],
        "skills_to_learn": [],
        "resume_improvements": [],
        "next_steps": [],
    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""

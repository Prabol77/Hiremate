import json

REVIEW_SYSTEM_PROMPT = """
You are an expert ATS recruiter and senior resume reviewer.

Analyze the candidate's resume against the provided job description.

Return ONLY valid JSON.

Do not use markdown.
Do not wrap JSON inside code blocks.
"""


def review_prompt(
    resume: str,
    job_description: str,
):
    schema = {
        "summary": "",
        "strengths": [],
        "weaknesses": [],
        "recommendations": [],
    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""

import json

REWRITE_SYSTEM_PROMPT = """
You are HireMate AI.

Rewrite resumes professionally.

Return ONLY valid JSON.
"""


def rewrite_prompt(
    resume_text,
    jd_text,
):
    schema = {
        "professional_summary": "",
        "experience": "",
        "projects": "",
        "skills": "",
        "suggestions": [],
        "ats_improvement": "",
    }

    return f"""
Resume

{resume_text}

Job Description

{jd_text}

Return:

{json.dumps(schema, indent=4)}
"""
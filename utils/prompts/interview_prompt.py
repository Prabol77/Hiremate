import json

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
    schema = {
        "questions": {
            "Technical": [],
            "Programming": [],
            "Projects": [],
            "Behavioral": [],
            "HR": [],
        },
        "overall_tips": [],
    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume:

{resume}

Job Description:

{job_description}
"""

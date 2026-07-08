"""
Interview Question Prompt.
"""

import json

# ==========================================================
# System Prompt
# ==========================================================

INTERVIEW_SYSTEM_PROMPT = """
You are a Senior Technical Interviewer and Hiring Manager.

Your task is to generate high-quality interview questions
based on the candidate's resume and the job description.

Rules:

1. Return ONLY valid JSON.
2. Do NOT wrap JSON inside markdown.
3. Do NOT add explanations.
4. Do NOT add text before or after JSON.
5. Generate practical, realistic interview questions.
6. Tailor every question to the candidate's resume.
7. Tailor every question to the target job description.
"""

# ==========================================================
# User Prompt
# ==========================================================


def interview_prompt(
    resume: str,
    job_description: str,
):
    """
    Build the interview generation prompt.
    """

    schema = {
        "questions": {
            "Technical": [
                "Question 1",
                "Question 2",
                "Question 3",
                "Question 4",
                "Question 5",
            ],
            "Programming": [
                "Question 1",
                "Question 2",
                "Question 3",
            ],
            "Projects": [
                "Question 1",
                "Question 2",
                "Question 3",
            ],
            "Behavioral": [
                "Question 1",
                "Question 2",
                "Question 3",
            ],
            "HR": [
                "Question 1",
                "Question 2",
                "Question 3",
            ],
        },
        "overall_tips": [
            "Tip 1",
            "Tip 2",
            "Tip 3",
        ],
    }

    return f"""
Generate interview questions for the following candidate.

Return JSON EXACTLY matching this schema.

{json.dumps(schema, indent=4)}

Requirements:

- Technical: 5 questions
- Programming: 3 questions
- Projects: 3 questions
- Behavioral: 3 questions
- HR: 3 questions
- Overall Tips: 3 interview tips

Candidate Resume:

{resume}

Job Description:

{job_description}
"""
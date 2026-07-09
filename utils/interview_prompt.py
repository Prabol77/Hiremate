import json


INTERVIEW_SYSTEM_PROMPT = """
You are an expert Technical Interviewer.

Return ONLY valid JSON.
Do not use markdown.
Do not explain anything.
Do not wrap the JSON in ``` blocks.
"""


def interview_prompt(
    resume_data,
    jd_text,
):

    candidate = {
        "domain": resume_data.metadata.get(
            "primary_domain",
            "General",
        ),
        "skills": resume_data.skills,
        "projects": [
            {
                "title": p.title,
                "description": p.description,
                "technologies": p.technologies,
            }
            for p in resume_data.projects
        ],
        "experience": [
            {
                "company": e.company,
                "role": e.role,
                "description": e.description,
            }
            for e in resume_data.experience
        ],
        "education": [
            edu.degree
            for edu in resume_data.education
        ],
    }

    schema = {
        "questions": {
            "Resume Specific": [
                "question1",
                "question2",
                "question3",
                "question4",
                "question5",
            ],
            "Technical": [
                "question1",
                "question2",
                "question3",
                "question4",
                "question5",
            ],
            "Projects": [
                "question1",
                "question2",
                "question3",
                "question4",
                "question5",
            ],
            "Behavioral": [
                "question1",
                "question2",
                "question3",
                "question4",
                "question5",
            ],
            "HR": [
                "question1",
                "question2",
                "question3",
                "question4",
                "question5",
            ],
        },
        "overall_tips": [
            "tip1",
            "tip2",
            "tip3",
            "tip4",
            "tip5",
        ],
    }

    return (
        "Candidate Information:\n\n"
        + json.dumps(candidate, indent=2)
        + "\n\nJob Description:\n\n"
        + jd_text
        + "\n\nReturn JSON matching exactly this schema:\n\n"
        + json.dumps(schema, indent=2)
    )
import json


CAREER_COACH_SYSTEM_PROMPT = """
You are HireMate AI Career Coach.

Your responsibility is to act as a professional career mentor.

You analyze:

- Resume
- ATS Analysis
- Skill Gap
- Career Readiness
- Hireability Score
- Recommended Projects

Provide practical, personalized advice.

Return ONLY valid JSON.

Do NOT include markdown.
"""


def career_coach_prompt(
    resume_data,
    ats_result,
    career,
    hireability,
    projects,
):

    candidate = {

        "Primary Domain": resume_data.metadata.get(
            "primary_domain",
            "General",
        ),

        "Hireability Score": hireability.overall,

        "Career Readiness": career.readiness_score,

        "Matched Skills": ats_result.matched_skills,

        "Missing Skills": ats_result.missing_skills,

        "Strengths": ats_result.strengths,

        "Weaknesses": ats_result.weaknesses,

        "Projects": [

            project.title

            for project in projects

        ],

    }

    schema = {

        "summary": "",

        "strengths": [],

        "focus_areas": [],

        "weekly_goals": [],

        "recommended_projects": [],

        "recommended_certifications": [],

        "interview_strategy": [],

        "final_message": "",

    }

    return f"""
Candidate Information

{json.dumps(candidate, indent=4)}

Return ONLY valid JSON.

Schema:

{json.dumps(schema, indent=4)}
"""
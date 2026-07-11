import json


PERSONALIZATION_SYSTEM_PROMPT = """
You are HireMate AI.

You receive already-computed career analysis.

Do NOT calculate scores.

Instead, explain the recommendations naturally.

Return ONLY valid JSON.

No markdown.
"""


def personalization_prompt(

    resume_data,

    career,

    hireability,

    projects,

    companies,

    certifications,

):

    candidate = {

        "Domain": resume_data.metadata.get(
            "primary_domain",
            "General",
        ),

        "Hireability": hireability.overall,

        "Projects": [

            project.title

            for project in projects

        ],

        "Companies": [

            company.company

            for company in companies[:5]

        ],

        "Certifications": [

            cert.name

            for cert in certifications

        ],

    }

    schema = {

        "career_summary": "",

        "why_projects": "",

        "why_certifications": "",

        "why_companies": "",

        "final_advice": "",

    }

    return f"""
Candidate

{json.dumps(candidate, indent=4)}

Return JSON

{json.dumps(schema, indent=4)}
"""
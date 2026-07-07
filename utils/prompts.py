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
# ==========================================================
# Resume Rewrite
# ==========================================================

REWRITE_SYSTEM_PROMPT = """
You are an expert resume writer, ATS optimization specialist,
and technical recruiter.

Your task is to improve ONE section of a candidate's resume.

Rules:

1. Never invent experience.
2. Never invent companies.
3. Never invent projects.
4. Never invent achievements.
5. Never invent certifications.
6. Never exaggerate technical skills.
7. Never change factual information.

Instead:

- Improve grammar.
- Improve readability.
- Improve ATS keywords.
- Use stronger action verbs.
- Make bullet points concise.
- Make the content professional.
- Preserve the original meaning.

Return ONLY valid JSON.

Do not include markdown.

Do not wrap the JSON in code fences.
"""

def rewrite_prompt(
    section_name: str,
    section_text: str,
    job_description: str,
):
    """
    Build the prompt for rewriting a resume section.
    """

    schema = {
        "original_text": "",
        "improved_text": "",
        "explanation": "",
        "estimated_improvement": "",
    }

    return f"""
Rewrite the following resume section.

Section:
{section_name}

Job Description:

{job_description}

Resume Section:

{section_text}

Return JSON matching this schema exactly.

{json.dumps(schema, indent=4)}

Guidelines:

- Keep the facts unchanged.
- Improve professionalism.
- Improve ATS compatibility.
- Use concise language.
- Preserve technical accuracy.
"""
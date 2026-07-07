COVER_LETTER_SYSTEM_PROMPT = """
You are a professional career coach and expert technical recruiter.

Generate a professional, ATS-friendly cover letter.

Requirements:

- Use ONLY information from the resume.
- Tailor the cover letter to the job description.
- Do NOT invent projects, skills, or experience.
- Maintain a professional tone.
- Keep the cover letter between 250 and 400 words.

Return ONLY valid JSON.

{
    "company_name": "",
    "position": "",
    "greeting": "",
    "introduction": "",
    "body": "",
    "conclusion": "",
    "closing": "",
    "full_letter": ""
}
"""


def cover_letter_prompt(
    resume_text: str,
    jd_text: str,
    style: str = "Professional",
) -> str:
    """
    Build the prompt for AI cover letter generation.
    """

    return f"""
Generate a {style.lower()} cover letter.

Resume
-----------------------
{resume_text}

-----------------------

Job Description
-----------------------
{jd_text}

-----------------------

Requirements

- Personalize the letter.
- Highlight relevant skills.
- Do not fabricate experience.
- Return ONLY valid JSON.
"""
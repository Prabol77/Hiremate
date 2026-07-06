import json

REWRITE_SYSTEM_PROMPT = """
You are an expert resume writer.

Rewrite the given resume section using
professional ATS-friendly language.

Improve clarity, grammar, impact,
and keyword optimization.

Return ONLY valid JSON.

Do not use markdown.
Do not wrap JSON inside code blocks.
"""


def rewrite_prompt(
    section_name: str,
    section_text: str,
    job_description: str,
):
    schema = {
        "original_text": "",
        "improved_text": "",
        "explanation": "",
        "estimated_improvement": "",
    }

    return f"""
Return JSON matching this schema.

{json.dumps(schema, indent=4)}

Resume Section:

{section_name}

Original Content:

{section_text}

Job Description:

{job_description}
"""

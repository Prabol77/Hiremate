"""
Utility functions for parsing JSON responses from LLMs.
"""

import json


def parse_llm_json(
    response: str,
) -> dict:
    """
    Safely parse a JSON response returned by an LLM.

    Automatically removes Markdown code fences if present.

    Args:
        response:
            Raw LLM response.

    Returns:
        Parsed dictionary.

    Raises:
        ValueError:
            If the response cannot be parsed.
    """

    cleaned = response.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.replace(
            "```json",
            "",
            1,
        )

    if cleaned.startswith("```"):
        cleaned = cleaned.replace(
            "```",
            "",
            1,
        )

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:

        return json.loads(
            cleaned,
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Unable to parse AI JSON response.\n\n{cleaned}"
        ) from error
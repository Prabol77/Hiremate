"""
Shared utilities for resume parsers.
"""

import re


class ParserUtils:
    """
    Common regex utilities.
    """

    EMAIL_PATTERN = (
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    PHONE_PATTERN = (
        r"(\+?\d[\d\s\-]{8,}\d)"
    )

    LINKEDIN_PATTERN = (
        r"(https?://)?(www\.)?linkedin\.com/[^\s]+"
    )

    GITHUB_PATTERN = (
        r"(https?://)?(www\.)?github\.com/[^\s]+"
    )

    URL_PATTERN = (
        r"https?://[^\s]+"
    )

    YEAR_PATTERN = (
        r"(19|20)\d{2}"
    )

    @staticmethod
    def clean_lines(
        text: str,
    ) -> list[str]:
        """
        Remove blank lines.
        """

        return [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]
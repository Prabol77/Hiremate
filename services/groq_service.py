from groq import Groq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)


class GroqService:
    """
    Generic wrapper around the Groq Chat API.
    """

    def __init__(self):

        if not GROQ_API_KEY:

            raise ValueError(
                "GROQ_API_KEY not found in .env"
            )

        self.client = Groq(
            api_key=GROQ_API_KEY,
        )

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Send a chat request to Groq.
        """

        response = self.client.chat.completions.create(

            model=GROQ_MODEL,

            temperature=TEMPERATURE,

            max_tokens=MAX_TOKENS,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt,
                },

                {
                    "role": "user",
                    "content": user_prompt,
                },

            ],
        )

        return (
            response
            .choices[0]
            .message
            .content
        )
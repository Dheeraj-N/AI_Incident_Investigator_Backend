from google import genai
from google.genai import errors as genai_errors

from app.core.settings import settings
from app.core.exceptions import GeminiRateLimitError


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    async def generate(
        self,
        prompt: str
    ) -> str:

        try:
            response = (
                self.client.models
                .generate_content(
                    model=settings.GEMINI_MODEL,
                    contents=prompt
                )
            )
            return response.text

        except genai_errors.ClientError as e:
            if e.code == 429:
                raise GeminiRateLimitError(
                    "Gemini API rate limit exceeded. Please try again later."
                ) from e
            raise
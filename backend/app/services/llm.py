import logging
from typing import Protocol

from ..config import settings

logger = logging.getLogger(__name__)


class LLMProvider(Protocol):
    async def generate(self, prompt: str) -> str:
        ...


class GeminiProvider:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.model_name = getattr(
            settings,
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        if not self.api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured. "
                "Set it in the backend .env file."
            )

        try:
            from google import genai

            self.client = genai.Client(
                api_key=self.api_key
            )

        except Exception as e:
            logger.exception("Failed to initialize Gemini client")
            raise RuntimeError(
                f"Failed to initialize Gemini client: {e}"
            ) from e

    async def generate(self, prompt: str) -> str:
        try:
            response = self.client.interactions.create(
                model=self.model_name,
                input=prompt
            )

            return response.output_text

        except Exception as e:
            logger.exception("Gemini API request failed")
            raise RuntimeError(
                f"Gemini API request failed: {e}"
            ) from e


def get_llm_provider() -> LLMProvider:
    provider = getattr(
        settings,
        "LLM_PROVIDER",
        "gemini"
    ).lower()

    if provider != "gemini":
        logger.warning(
            "Unsupported LLM provider '%s'; falling back to Gemini.",
            provider
        )

    return GeminiProvider()
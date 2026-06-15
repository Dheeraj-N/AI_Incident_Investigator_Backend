from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATA_SOURCE: str = "mock"
    OPENAI_API_KEY: str = ""
    LOG_LEVEL: str = "INFO"
    APP_ENV: str = "development"
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = (
        "gemini-2.5-flash"
    )

    class Config:
        env_file = ".env"


settings = Settings()
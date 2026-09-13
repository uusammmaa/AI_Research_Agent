from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    anthropic_api_key: str
    tavily_api_key: str
    model: str = "claude-sonnet-4-20250514"
    max_iterations: int = 10
    cors_origins: str = "http://localhost:3000"


settings = Settings()


def get_cors_origins() -> list[str]:
    return [origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()]

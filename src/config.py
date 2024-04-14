from pydantic import AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_connection_string: PostgresDsn
    exchange_url: AnyHttpUrl = "https://api.kucoin.com/"
    app_host: str
    app_port: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()

__all__ = ["settings"]

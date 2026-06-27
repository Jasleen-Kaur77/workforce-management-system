from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Workforce Management System"
    app_version: str = "1.0.0"

    database_url: str

    secret_key: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
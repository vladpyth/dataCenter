from dotenv import load_dotenv

load_dotenv()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str = "your-secret-key"  # Добавьте это
    JWT_ALGORITHM: str = "HS256"

    access_token_expire_minutes: int
    refresh_token_expire_days: int

    @property
    def DATABASE_URL(self):
        # "postgresql+psycopg://postgres:postgres@localhost:5438/postgres"
        # "postgresql + asyncpg: // postgres @ localhost: 5432 / dast"
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str = "dev_secret_key"
    JWT_ALGORITHM: str = "HS256"


    class Config:
        env_file = ".env"

settings = Settings()


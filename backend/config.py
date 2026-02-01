import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')

settings = Settings(os.environ)


def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}
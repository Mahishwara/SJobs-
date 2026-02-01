import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    def __init__(self, data):
        POSTGRES_USER: data['POSTGRES_USER']
        POSTGRES_PASSWORD: data['POSTGRES_PASSWORD']
        POSTGRES_DB: data['POSTGRES_DB']
        POSTGRES_HOST: data['POSTGRES_HOST']
        POSTGRES_PORT: data['POSTGRES_PORT']
        SECRET_KEY: data['SECRET_KEY']
        ALGORITHM: data['ALGORITHM']


settings = Settings(os.environ)


def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}
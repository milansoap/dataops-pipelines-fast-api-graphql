# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "localhost"
    database: str = "postgres"
    username: str = "soap"
    password: str = "Samsung123@"
    port: int = 5432

conn_settings = Settings()
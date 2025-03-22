from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "localhost"
    database: str = "postgres"
    user: str = "soap"
    password: str = "Samsung123@"
    port: int = 5432

conn_settings = Settings()


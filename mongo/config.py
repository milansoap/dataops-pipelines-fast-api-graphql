from pydantic_settings import BaseSettings

class MongoSettings(BaseSettings):
    host: str = "localhost"
    port: int = 27017

mongo_conn_settings = MongoSettings()

print(mongo_conn_settings.port)
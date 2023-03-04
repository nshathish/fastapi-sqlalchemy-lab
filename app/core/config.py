from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "My App"
    API_V1_STR: str = "/api/v1"
    API_V2_STR: str = "/api/v2"
    SQLALCHEMY_DATABASE_URI: str = "sqlite+pysqlite:///mydb.db"


settings = Settings()

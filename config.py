from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    BASE_URL: str

    class Config:
        env_file = ".env"
setting = Settings()

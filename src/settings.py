from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqs_access: str
    sqs_secret: str

    model_config = SettingsConfigDict(env_file='src/.env')


settings = Settings()
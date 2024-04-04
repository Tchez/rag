from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    PINECONE_API_KEY: str
    PINECONE_METRIC: str
    PINECONE_INDEX: str

    OPENAI_EMBEDDING_MODEL: str
    OPENAI_API_KEY: str

    EMBEDDING_DIMENSIONS: int

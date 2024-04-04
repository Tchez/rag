from typing import List

from fastapi import UploadFile
from langchain_openai import OpenAIEmbeddings

from rag.settings import Settings

settings = Settings()


def to_embedding(files: List[UploadFile]) -> List[float] | None:
    embed_model = OpenAIEmbeddings(
        model=settings.OPENAI_EMBEDDING_MODEL,
        dimensions=settings.EMBEDDING_DIMENSIONS,
    )
    files: List[str] = [file.decode() for file in files]
    embeddings = embed_model.embed_documents(files)

    return embeddings if embeddings else None

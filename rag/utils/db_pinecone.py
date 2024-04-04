from pinecone import Index, Pinecone

from rag.settings import Settings

settings = Settings()


def get_index() -> Index:
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)

    try:
        index = pc.Index(name=settings.PINECONE_INDEX)
        if (
            index.describe_index_stats()['dimension']
            != settings.EMBEDDING_DIMENSIONS
        ):
            raise Exception(
                'A dimensão do índice não corresponde à dimensão do vetor de embedding'
            )
    except Exception as e:
        raise Exception(f'Erro ao conectar ao índice: {e}')

    return index

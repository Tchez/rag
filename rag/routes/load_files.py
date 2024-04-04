from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

from rag.schemas.api_response import ResponseLoadFiles
from rag.utils.db_pinecone import Index, get_index
from rag.utils.embedding import to_embedding

router = APIRouter()


@router.post(
    '/load-files',
    tags=['Carregar Arquivos de texto no banco de dados'],
    response_model=ResponseLoadFiles,
)
async def load_files(
    files: List[UploadFile],
    index: Index = Depends(get_index),
) -> ResponseLoadFiles:
    """Recebe um ou mais arquivos, transforma em vetores e carrega no banco de dados vetorial.
    Levanta uma exceção HTTP se não puder conectar ao banco de dados ou se não conseguir carregar os arquivos.
    """
    try:
        if not index:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Erro ao carregar arquivos: não foi possível conectar ao banco de dados',
            )

        print(index.describe_index_stats())
        breakpoint()
        files = [await file.read() for file in files]
        embedding = to_embedding(files)

        if not embedding:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Erro ao carregar arquivos: não foi possível gerar vetores de embedding',
            )

        index.upsert(items=files, vectors=embedding)
        return {
            'message': message,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao carregar arquivos: {e}',
        )

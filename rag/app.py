from fastapi import FastAPI

from rag.routes.index import router as root_router
from rag.routes.load_files import router as load_files_router

app = FastAPI(
    title='Rag API',
    description='Aplicação RAG para meu TCC',
    version='0.1.0',
    docs_url='/docs',
    redoc_url='/redoc',
)

app.include_router(root_router)
app.include_router(load_files_router)

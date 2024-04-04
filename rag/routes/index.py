from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get('/', include_in_schema=False)
def read_root():
    """
    Redireciona as requisições da raiz ("/") para a documentação do Swagger UI em "/openapi.json".

    Returns:
        response: A instância do RedirectResponse apontando para "/openapi.json".
    """
    response = RedirectResponse(url='/openapi.json')
    return response

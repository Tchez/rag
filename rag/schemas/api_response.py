from pydantic import BaseModel


class ResponseLoadFiles(BaseModel):
    message: str

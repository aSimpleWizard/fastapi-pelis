from typing import Optional
from pydantic import BaseModel

class Pelicula(BaseModel):
    pelicula_id: Optional[int]
    nombre : str
    fecha : str
    comentario: str

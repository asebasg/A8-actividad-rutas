from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    id: int
    nombre: str = Field(..., min_length=3) # Indica campo requerido
    precio: float = Field(..., gt=0) # "gt" es para mayor que, "lt" para menor que
    descripcion: Optional[str] = None
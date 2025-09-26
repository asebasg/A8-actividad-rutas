# Importaciones de Pydantic para definir modelos de datos con validación automática
from pydantic import BaseModel, Field
from typing import Optional  # Para tipos opcionales en Python

# Define el modelo de datos para un Producto, heredando de BaseModel para validación automática
class Producto(BaseModel):
    # Campo obligatorio para el identificador único del producto, debe ser un entero
    id: int
    # Campo obligatorio para el nombre del producto, con validación de longitud mínima de 3 caracteres
    nombre: str = Field(..., min_length=3)  # Indica que es requerido y establece la longitud mínima
    # Campo obligatorio para el precio, debe ser un flotante mayor que 0
    precio: float = Field(..., gt=0)  # "gt" significa greater than, asegura que el precio sea positivo
    # Campo opcional para la descripción del producto, puede ser None si no se proporciona
    descripcion: Optional[str] = None

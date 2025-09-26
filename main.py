# Importaciones necesarias para crear la aplicación FastAPI y manejar rutas
from fastapi import FastAPI
from routers import productos  # Importa el módulo de rutas de productos
import uvicorn  # Servidor ASGI para ejecutar la aplicación

# Creación de la instancia principal de FastAPI, que será el núcleo de la API
app = FastAPI()

# Incluye el router de productos en la aplicación principal, permitiendo que las rutas definidas en productos.py estén disponibles
app.include_router(productos.router)

# Define un endpoint raíz (GET en "/") que devuelve un mensaje de bienvenida simple
@app.get("/")
def inicio():
    return {"mensaje": "API de Productos"}

# Bloque que se ejecuta solo si el archivo se corre directamente, iniciando el servidor con recarga automática para desarrollo
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

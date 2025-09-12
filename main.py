from fastapi import FastAPI
from routers import productos
import uvicorn

app = FastAPI()
app.include_router(productos.router)

@app.get("/")
def inicio():
    return {"mensaje": "API de Productos"}

# * Inicializa el servidor automaticamente
if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
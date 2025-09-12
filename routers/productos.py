from fastapi import APIRouter,HTTPException
from models import Producto
from fastapi.responses import HTMLResponse

router = APIRouter() # * Ruta independiente

producto_db = []

@router.get("/productos", response_class=HTMLResponse)
def obtener_producto():
    if not producto_db:
        return "<h2 style='color: red; font-family: Arial; text-align: center; margin: 40px'>❌ No hay productos disponibles</h2>"
    
    html = """
                <html lang="en">

        <head>
            <title>Listado de productos</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }

                h1 {
                    color: #333;
                    text-align: center;
                }

                table {
                    width: 60%;
                    border-collapse: collapse;
                    background-color: white;
                    margin: 20px;
                }

                th,
                td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: center;
                }

                ul {
                    list-style-type: none;
                    padding: 0;
                }

                li {
                    background: #f4f4f4;
                    margin: 5px 0;
                    padding: 10px;
                    border-radius: 5px;
                }
            </style>
        </head>

        <body>
            <h1>🛒 Listado de productos 📣</h1>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Precio</th>
                    <th>Descripcion</th>
                </tr>
    """

    for p in producto_db:
        html += f"""
                <tr>
                    <td>{p.id}</td>
                    <td>{p.nombre}</td>
                    <td>{p.precio}</td>
                    <td>{p.descripcion if p.descripcion else "No hay descripcion."}</td>
                </tr>
        """
    html += """</table> </body> </html>"""
    return HTMLResponse(content=html, status_code=200)

@router.post("/productos")
def crear_producto(producto: Producto):
    # Validación de duplicado por ID, se detiene al encontrar la primera coincidencia True (usando el any)
    if any(p.id == producto.id for p in producto_db):
        raise HTTPException(status_code=409, detail=f"El producto con ID {producto.id} ya existe")
    producto_db.append(producto)
    return {"text:": f"¡Hecho! Producto: {producto.nombre} creado exitosamente"}  # Utiliza clases y objetos para manejar datos

@router.put("/productos/{id}")
def reemplazar_producto(id: int, producto: Producto):
    if id not in producto_db:
        return {"Error:": f"Producto con id {producto.id} no encontrado"}
    producto_db[id] = producto
    return {
        "text:": "¡Hecho! Producto actualizado",
        "Nuevo producto:" : f"{producto.nombre}"
    }

@router.patch("/productos/{id}")
def complementar_producto(id: int, texto: str, producto: Producto):
    if id not in producto_db:
        return {"Error": f"El prodcuto con ID {producto.id} no encontrado"}
    producto_db[id] += " " + texto
    return {
        "text:": "¡Hecho! Producto actualizado",
        "Producto actualizado:" : f"{producto.nombre}"
    }

@router.patch("/productos/{id}")
def eliminar_producto(id: int, producto: Producto):
    if id not in producto_db:
        return {"Error": f"El prodcuto con ID {producto.id} no encontrado"}
    del producto_db[id]
    return {
        "text:": "¡Hecho! Producto eliminado"
    }
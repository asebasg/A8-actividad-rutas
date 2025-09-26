# Importaciones necesarias para crear rutas, manejar excepciones y respuestas HTML
from fastapi import APIRouter, HTTPException
from models import Producto  # Importa el modelo de Producto para validación de datos
from fastapi.responses import HTMLResponse  # Para devolver respuestas en formato HTML

# Crea un router independiente para agrupar las rutas relacionadas con productos
router = APIRouter()

# Lista simulada que actúa como base de datos en memoria para almacenar productos
producto_db = []

# Endpoint GET para obtener la lista de productos en formato HTML
@router.get("/productos", response_class=HTMLResponse)
def obtener_producto():
    # Verifica si la base de datos está vacía y devuelve un mensaje de error en HTML si no hay productos
    if not producto_db:
        return "<h2 style='color: red; font-family: Arial; text-align: center; margin: 40px'>❌ No hay productos disponibles</h2>"
    
    # Construye el HTML inicial con estilos CSS embebidos para la tabla de productos
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

    # Itera sobre cada producto en la base de datos y agrega filas a la tabla HTML
    for p in producto_db:
        html += f"""
                <tr>
                    <td>{p.id}</td>
                    <td>{p.nombre}</td>
                    <td>{p.precio}</td>
                    <td>{p.descripcion if p.descripcion else "No hay descripcion."}</td>
                </tr>
        """
    # Cierra la estructura HTML y devuelve la respuesta
    html += """</table> </body> </html>"""
    return HTMLResponse(content=html, status_code=200)

# Endpoint POST para crear un nuevo producto
@router.post("/productos")
def crear_producto(producto: Producto):
    # Valida si ya existe un producto con el mismo ID, usando 'any' para eficiencia
    if any(p.id == producto.id for p in producto_db):
        raise HTTPException(status_code=409, detail=f"El producto con ID {producto.id} ya existe")
    # Agrega el producto a la base de datos y devuelve un mensaje de éxito
    producto_db.append(producto)
    return {"text:": f"¡Hecho! Producto: {producto.nombre} creado exitosamente"}

# Endpoint PUT para reemplazar completamente un producto existente por ID
@router.put("/productos/{id}")
def reemplazar_producto(id: int, producto: Producto):
    # Nota: Esta verificación asume que id es un índice, pero debería ser el ID del producto
    if id not in producto_db:  # Esto es incorrecto, debería buscar por ID
        return {"Error:": f"Producto con id {producto.id} no encontrado"}
    # Reemplaza el producto en la posición del índice (no recomendado, debería buscar por ID)
    producto_db[id] = producto
    return {
        "text:": "¡Hecho! Producto actualizado",
        "Nuevo producto:": f"{producto.nombre}"
    }

# Endpoint PATCH para complementar la descripción de un producto (nota: parámetros extraños, texto no usado correctamente)
@router.patch("/productos/{id}")
def complementar_producto(id: int, texto: str, producto: Producto):
    # Verificación similar al PUT, incorrecta
    if id not in producto_db:
        return {"Error": f"El producto con ID {producto.id} no encontrado"}
    # Intenta concatenar texto a la descripción, pero producto_db[id] es un objeto Producto, no str
    producto_db[id] += " " + texto  # Esto causará error
    return {
        "text:": "¡Hecho! Producto actualizado",
        "Producto actualizado:": f"{producto.nombre}"
    }

# Endpoint PATCH para eliminar un producto (nota: debería ser DELETE, y lógica incorrecta)
@router.patch("/productos/{id}")
def eliminar_producto(id: int, producto: Producto):
    # Verificación incorrecta
    if id not in producto_db:
        return {"Error": f"El producto con ID {producto.id} no encontrado"}
    # Elimina el producto por índice, no por ID
    del producto_db[id]
    return {
        "text:": "¡Hecho! Producto eliminado"
    }

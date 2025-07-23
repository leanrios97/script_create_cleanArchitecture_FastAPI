main = """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "Mi Proyecto FastAPI",
    description = "Estructura de una API RESTful con clean architecture",
    version = "0.1.0",
    openapi_tags=[
        {
            "name": "Estructura inicial",
            "description": "Estructura inicial"
        },
        # Agregar tags
        ],
    docs_url = "/api/docs", # Documentación Swagger IU
    redoc_url = "/api/redoc", # Documentación Redoc
    openapi_url="/api/openapi.json",  # URL para el schema OpenAPI
    servers=[
        {"url": "http://localhost:8000", "description": "Servidor local"},
        {"url": "dominio produccion", "description": "Servidor en producción"}, # Remplazar url por producción.
        ]
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"], # Permite todos los origenes para desarrollo.
                           # En producción se debera especificar los dominios permitidos.
    allow_credentials = True, 
    allow_methods = ["*"], # Permite todos los metodos HTTP
    allow_headers = ["*"], # Permite todos los encabezados
)

# Aca para incluir rutas
# app.include_router( modulo.router, prefix = "/api/modulo", tags = ["Modulo nombre"])

@app.get("/api", tags=['Root'])
async def read_root():
    return {"message": "Bienvenido a mi API FastAPI!"}
"""


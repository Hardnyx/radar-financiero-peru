Backend de Radar Financiero Perú.

Framework: FastAPI.

Endpoints actuales:

GET /
Devuelve información general de la API.

GET /health
Devuelve el estado básico del backend.

series
Diccionario temporal con la información de las series.

GET /api/series
Devuelve las claves disponibles del diccionario.

GET /api/series/{code}
Busca una clave específica dentro del diccionario.

Si existe:
    devuelve la serie.

Si no existe:
    devuelve 404.
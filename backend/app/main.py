from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Radar Financiero Perú API",
    description="API para consultar información macroeconómica, financiera y regulatoria de fuentes públicas peruanas.",
    version="0.1.0"
)

ECONOMIC_SERIES = {
    "bcrp-policy-rate": {
        "code": "bcrp-policy-rate",
        "name": "Tasa de referencia BCRP",
        "source": "BCRP",
        "frequency": "monthly",
        "unit": "percent",
        "description": "Tasa de política monetaria del Banco Central de Reserva del Perú."
    },
    "exchange-rate": {
        "code": "exchange-rate",
        "name": "Tipo de cambio",
        "source": "BCRP",
        "frequency": "daily",
        "unit": "PEN per USD",
        "description": "Tipo de cambio promedio del sol peruano frente al dólar estadounidense."
    },
    "monthly-inflation": {
        "code": "monthly-inflation",
        "name": "Inflación mensual",
        "source": "BCRP",
        "frequency": "monthly",
        "unit": "percent",
        "description": "Variación mensual del índice de precios al consumidor."
    }
}

@app.get("/", tags = ["System"])
async def root():
    return {
        "status": "ok",
        "service": "radar-financiero-peru-api",
        "version": "0.1.0"
    }


@app.get("/health", tags = ["System"])
async def health_check():
    return {
        "status": "ok"
    }

@app.get("/api/series", tags=["Economic Series"])
async def list_economic_series():
    return {
        "total": len(ECONOMIC_SERIES),
        "series": list(ECONOMIC_SERIES.values())
    }

@app.get("/api/series/{code}", tags=["Economic Series"])
async def get_economic_series_by_code(code: str):
    if code in ECONOMIC_SERIES:
        return ECONOMIC_SERIES[code]
    
    raise HTTPException(
        status_code=404,
        detail="Economic series not found"
    )
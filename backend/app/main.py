from fastapi import FastAPI, HTTPException

app = FastAPI()

series = {
    "bcrp-policy-rate" : {
        "code": "bcrp-policy-rate",
        "name": "Tasa de referencia BCRP",
        "source": "BCRP",
        "frequency": "monthly",
        "unit": "percent",
        "description": "Tasa de política monetaria del Banco Central de Reserva del Perú."
    },
    "exchange-rate" : {
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

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "radar-financiero-peru-api",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "ok"
    }

@app.get("/api/series")
async def list_available_series():
    return {
        "series": list(series.values())
    }

@app.get("/api/series/{code}")
async def get_series_by_code(code: str):
    if code in series:
        return series[code]
    else:
        raise HTTPException(status_code=404, detail= "Economic series not found")
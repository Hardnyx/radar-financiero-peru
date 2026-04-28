from fastapi import FastAPI

app = FastAPI()

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
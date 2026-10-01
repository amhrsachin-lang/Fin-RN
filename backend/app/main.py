from fastapi import FastAPI

from app.routers import market, trade

app = FastAPI(title="Virtual Trading API")

app.include_router(market.router, prefix="/api")
app.include_router(trade.router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}

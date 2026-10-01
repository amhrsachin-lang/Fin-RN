from fastapi import APIRouter

router = APIRouter()


@router.get("/search")
def search(q: str):
    # TODO: query MFapi.in (mutual funds) and yfinance (stocks)
    return {"results": []}


@router.get("/asset/{ticker}")
def get_asset(ticker: str):
    # TODO: return market price, day-change %, and chart data
    return {"ticker": ticker, "price": None, "changePct": None, "chart": []}

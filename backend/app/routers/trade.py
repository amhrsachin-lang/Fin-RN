from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TradeRequest(BaseModel):
    uid: str
    assetTicker: str
    assetType: Literal["STOCK", "MUTUAL_FUND"]
    type: Literal["BUY", "SELL"]
    quantity: float


@router.post("/trade")
def trade(req: TradeRequest):
    # TODO: validate liquidBalance, update holdings, write transaction to Firestore
    return {"status": "not_implemented", "request": req}

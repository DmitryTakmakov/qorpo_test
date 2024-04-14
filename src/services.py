import urllib.parse

import aiohttp
from src.config import settings


async def get_exchange_rate_for_currency(currency: str) -> float:
    url = str(settings.exchange_url) + "api/v1/market/candles?"
    currency = currency.upper()
    symbol = f"{currency}-USDT"
    params = {
        "symbol": symbol,
        "type": "15min",
    }
    url = url + urllib.parse.urlencode(params)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp_data = await resp.json()
            code = int(resp_data["code"])
            if code != 200000:
                raise ValueError(resp_data["msg"])
            market_data = resp_data["data"]
        await session.close()
    return float(market_data[-1][2])


__all__ = ["get_exchange_rate_for_currency"]

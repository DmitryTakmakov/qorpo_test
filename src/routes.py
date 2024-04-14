from aiohttp import web
from src.db.orm import CurrencyDAO
from src.services import get_exchange_rate_for_currency


async def get_price(request: web.Request) -> web.Response:
    currency = request.match_info["currency"]
    try:
        rate = await get_exchange_rate_for_currency(currency)
    except ValueError as e:
        return web.json_response({"Error": str(e)}, status=400)
    dao = CurrencyDAO(request.app["db"])
    await dao.create(currency=currency, price=rate)
    return web.json_response({"price": rate})


async def get_price_history(request: web.Request) -> web.Response:
    page = request.query.get("page")
    if page is None:
        return web.json_response({"Error": "Page is a required query parameter."})
    page = int(page)
    dao = CurrencyDAO(request.app["db"])
    if page != 1:
        offset = page * 10 + 1
    else:
        offset = 1
    results = await dao.list(offset=offset)
    return web.json_response({"results": results})


async def delete_price_history(request: web.Request) -> web.Response:
    dao = CurrencyDAO(request.app["db"])
    await dao.flush_table()
    return web.Response(status=204)


def setup_routes(app: web.Application):
    app.router.add_get("/price/history", get_price_history, name="price-history")
    app.router.add_delete("/price/history", delete_price_history, name="price-history-delete")
    app.router.add_get("/price/{currency}", get_price, name="price")


__all__ = ["setup_routes"]

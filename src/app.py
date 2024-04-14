from aiohttp import web
from src.db.session import pg_context
from src.routes import setup_routes


async def web_app():
    app = web.Application()
    app.cleanup_ctx.append(pg_context)

    setup_routes(app)

    return app

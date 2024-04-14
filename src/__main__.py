from aiohttp import web
from src.app import web_app
from src.config import settings

app = web_app()
web.run_app(app, host=settings.app_host, port=settings.app_port)

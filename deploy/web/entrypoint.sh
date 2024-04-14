#!/bin/bash
alembic -c src/alembic.ini upgrade head
gunicorn src.app:web_app --bind 0.0.0.0:80 --worker-class aiohttp.GunicornWebWorker

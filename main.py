import os
import sys

from aiohttp import web

from multiplier.routes import routes
from web import app

if __name__ == '__main__':
    application = app.init(routes=routes)

    port = os.environ.get("SERVER_PORT")
    web.run_app(application, port=port)

import os

os.environ["SOLARA_APP"] = "pages/__init__.py"

import uvicorn
import solara.server.starlette
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount


# os.environ["APP_MODULE"] = "main:app"

app = solara.server.starlette.app

if __name__ == "__main__":
    print("Starting app ", os.environ["SOLARA_APP"])
    uvicorn.run(app, host="0.0.0.0", port=8000)
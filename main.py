import os

import solara.server.starlette
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount


# os.environ["SOLARA_APP"] = "pages/__init__.py"

def myroot(request: Request):
    return JSONResponse({"framework": "solara"})

routes = [
    Route("/", myroot),
    # Mount("/solara", routes=solara.server.starlette.routes)
]

app = Starlette(routes=routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
import os

os.environ["SOLARA_APP"] = "pages/__init__.py"

from fastapi import FastAPI
import uvicorn
import solara.server.starlette


app = FastAPI()

@app.get("/")
def read_root():
    return {"framework": "solara"}

app.mount("/solara", solara.server.starlette.app)

# app = solara.server.starlette.app

if __name__ == "__main__":
    print("Starting app ", os.environ["SOLARA_APP"])
    uvicorn.run(app, host="0.0.0.0", port=8000)
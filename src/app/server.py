from sanic import Sanic, Request
from sanic.response import text

app = Sanic("Start")
app.config.TEMPLATING_PATH_TO_TEMPLATES = ["src/templates"]


@app.get("/")
@app.ext.template("index.html")
async def index(request: Request):
    return {"title": "Start"}

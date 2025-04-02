from sanic import Sanic
from sanic.response import text

app = Sanic("Start")


@app.get("/")
async def index(request):
    return text("loves ya")

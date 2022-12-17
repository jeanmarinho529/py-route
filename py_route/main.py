from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .handler import Route
from .model import Geolocation, Points
from .model import Route as RouteModel

app = FastAPI(
    title="Py Route",
    description="d",
    version="0.1.0",
    contact={
        "name": "Jean Marinho",
        "url": "http://x-force.example.com/contact/",
        "email": "jeanmarinho529@gmail.com",
    },
)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.post("/", response_model=RouteModel)
async def route(points: Points):
    return await Route.process(points)

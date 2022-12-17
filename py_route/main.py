from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .config import settings
from .handler import Route
from .model import Geolocation, Points
from .model import Route as RouteModel

app = FastAPI(
    title=settings.APP_NAME,
    description="d",
    version=settings.VERSION,
    contact={
        "name": "Jean Marinho",
        "url": "http://x-force.example.com/contact/",
        "email": settings.ADMIN_EMAIL,
    },
)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.post("/", response_model=RouteModel)
async def route(points: Points):
    return await Route.process(points)

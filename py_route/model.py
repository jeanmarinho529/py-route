from pydantic import BaseModel, validator

from .config import settings


class Geolocation(BaseModel):
    lat: float
    long: float


class Point(BaseModel):
    origin: Geolocation
    destinations: list[Geolocation]

    @validator("destinations")
    def _check_maximum_qty(cls, v) -> list[Geolocation]:
        if len(v) > settings.MAX_POINTS:
            raise ValueError("maximum number of locations reached")
        return v


class Route(BaseModel):
    distance_value: float
    distance_unit: str = "meter"
    origin: Geolocation
    destinations: list[Geolocation]

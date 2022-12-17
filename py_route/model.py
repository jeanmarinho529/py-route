from pydantic import BaseModel, Field, validator

from .config import settings


class Geolocation(BaseModel):
    lat: float = Field(title="dddd")
    long: float


class Points(BaseModel):
    origin: Geolocation
    destinations: list[Geolocation]
    destination_points: list[tuple[float, float]] = []

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

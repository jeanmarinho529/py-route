import pytest


@pytest.fixture
def geolocation_data():
    return {"lat": -5.4025803, "long": -36.954107}


@pytest.fixture
def point_data(geolocation_data):
    return {
        "origin": geolocation_data,
        "destinations": [
            {"lat": -5.4025803, "long": -36.954107},
            {"lat": -5.3025800, "long": -36.854107},
        ],
    }


@pytest.fixture
def route_data(geolocation_data):
    return {
        "distance_value": 15656.88,
        "distance_unit": "meter",
        "origin": geolocation_data,
        "destinations": [
            {"lat": -5.4025803, "long": -36.954107},
            {"lat": -5.3025800, "long": -36.854107},
        ],
    }


@pytest.fixture
def points():
    return [(-5.4025803, -36.954107), (-5.30258, -36.854107)]


@pytest.fixture
def combination_all_points():
    return [
        ((-5.4025803, -36.954107), (-5.30258, -36.854107)),
        ((-5.30258, -36.854107), (-5.4025803, -36.954107)),
    ]

import pytest
from pydantic.error_wrappers import ValidationError

from py_route.config import settings
from py_route.model import Geolocation, Point, Route


def test_should_create_geolocation(geolocation_data):
    geolocation = Geolocation(**geolocation_data)

    assert geolocation.dict() == geolocation_data


@pytest.mark.parametrize("key", ("lat", "long"))
def test_transaction_not_null_values_geolocation(geolocation_data, key):
    geolocation_data[key] = None
    with pytest.raises(ValidationError) as exec_info:
        Geolocation(**geolocation_data)

    assert exec_info.value.errors()[0]["msg"] == "none is not an allowed value"


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    (
        ("lat", [], "value is not a valid float"),
        ("long", [], "value is not a valid float"),
    ),
)
def test_transaction_typing_geolocation(geolocation_data, key, value, expected):
    geolocation_data[key] = value
    with pytest.raises(ValidationError) as exec_info:
        Geolocation(**geolocation_data)

    assert exec_info.value.errors()[0]["msg"] == expected


def test_should_create_point(point_data):
    point = Point(**point_data)

    assert point.dict() == point_data


@pytest.mark.parametrize("key", ("origin", "destinations"))
def test_should_check_whether_attributes_required_point(point_data, key):
    point_data[key] = None
    with pytest.raises(ValidationError) as exec_info:
        Point(**point_data)

    assert exec_info.value.errors()[0]["msg"] == "none is not an allowed value"


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    (
        ("origin", [], "field required"),
        ("destinations", "", "value is not a valid list"),
    ),
)
def test_transaction_typing_point(point_data, key, value, expected):
    point_data[key] = value
    with pytest.raises(ValidationError) as exec_info:
        Point(**point_data)

    assert exec_info.value.errors()[0]["msg"] == expected


def test_should_throw_maximum_number_destinations_exception(point_data):
    with pytest.raises(ValidationError) as exec_info:
        settings.MAX_POINTS = 1
        Point(**point_data)

    assert exec_info.value.errors()[0]["msg"] == "maximum number of locations reached"


def test_should_create_route(route_data):
    route = Route(**route_data)

    assert route.dict() == route_data


@pytest.mark.parametrize(
    "key", ("distance_value", "distance_unit", "origin", "destinations")
)
def test_should_check_whether_attributes_required_route(route_data, key):
    route_data[key] = None
    with pytest.raises(ValidationError) as exec_info:
        Route(**route_data)

    assert exec_info.value.errors()[0]["msg"] == "none is not an allowed value"


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    (
        ("distance_value", [], "value is not a valid float"),
        ("distance_unit", [], "str type expected"),
        ("origin", [], "field required"),
        ("destinations", "", "value is not a valid list"),
    ),
)
def test_transaction_typing_route(route_data, key, value, expected):
    route_data[key] = value
    with pytest.raises(ValidationError) as exec_info:
        Route(**route_data)

    assert exec_info.value.errors()[0]["msg"] == expected

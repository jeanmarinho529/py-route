import pytest

from py_route.handler import Route
from py_route.model import Point
from py_route.model import Route as RouteModel


@pytest.mark.asyncio
async def test_should_enter_points_return_route(point_data, route_data):
    point = Point(**point_data)
    route = RouteModel(**route_data)

    assert await Route.process(point) == route


@pytest.mark.asyncio
async def test_should_convert_dict_to_list(points, point_data):
    point = Point(**point_data)

    assert await Route._destination_points(point) == points


@pytest.mark.asyncio
async def test_should_return_combination_all_points(points, combination_all_points):
    assert await Route._all_combinations(points) == combination_all_points


@pytest.mark.asyncio
async def test_should_create_best_route(combination_all_points, point_data, route_data):
    point = Point(**point_data)
    route = RouteModel(**route_data)

    assert await Route._calculate_distances(combination_all_points, point) == route

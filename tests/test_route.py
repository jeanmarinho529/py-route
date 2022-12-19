from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from py_route.main import app

client = TestClient(app)


def test_pong():
    response = client.get("/ping/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"ping": "pong!"}


@pytest.mark.asyncio
async def test_main():
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.url == "http://testserver/docs"


@pytest.mark.asyncio
async def test_docs():
    response = client.get("/docs/")

    assert response.status_code == HTTPStatus.OK


@pytest.mark.asyncio
async def test_route(point_data, route_data):
    response = client.post("/", json=point_data)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == route_data


@pytest.mark.asyncio
async def test_route_unprocessable():
    response = client.post("/", json={})

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "origin"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "destinations"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }

from itertools import permutations

from geopy.distance import geodesic

from .model import Geolocation, Point
from .model import Route as RouteModel


class Route:
    async def process(point: Point) -> RouteModel:
        destination_points = await Route._format_destination_points(point)
        combinations = await Route._all_destination_combinations(destination_points)
        return await Route._find_best_route(combinations, point)

    async def _format_destination_points(point: Point) -> list[tuple]:
        destination_points = []
        for geo in point.destinations:
            destination_points.append(tuple((geo.lat, geo.long)))

        return destination_points

    async def _all_destination_combinations(geolocations: list[tuple]) -> list[tuple]:
        combinations = []
        [combinations.append(geo) for geo in list(permutations(geolocations))]
        return combinations

    async def _find_best_route(geolocations: list[tuple], points: Point) -> RouteModel:
        starting_point = (points.origin.lat, points.origin.long)

        final_distance = None
        final_sequence = []

        for sequence in geolocations:
            last_point = starting_point
            sequence_distance = 0

            for point in sequence:
                sequence_distance += float(geodesic(last_point, point).meters)
                last_point = point

            if final_distance is None or sequence_distance < final_distance:
                final_distance = sequence_distance
                final_sequence = [Geolocation(lat=s[0], long=s[1]) for s in sequence]

        return RouteModel(
            distance_value=round(final_distance, 2),
            origin=points.origin,
            destinations=final_sequence,
        )

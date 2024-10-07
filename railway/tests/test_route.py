import pytest
from railway.route import Route
from railway.tests.test_data import BaseSetUp


class TestRoute(BaseSetUp):

    def test_route_is_valid(self, stations):
        assert Route(stations[2], stations[3])

    def test_route_is_not_valid(self, stations):
        with pytest.raises(ValueError, match="Route's start or end must be an object of Station class."):
            Route('Kyiv', 'Zhytomyr')

    def test_route_repr(self, routes):
        expected_repr = "Route(start=Station(name='Kyiv'), end=Station(name='Yalta'))"
        assert repr(routes[2]) == expected_repr

    def test_route_get_way(self, routes, stations):
        assert 'Kyiv', 'Yalta' in routes[2].get_way()

    def test_route_add_way(self, routes, stations):
        routes[0].add_intermediate_station(stations[3])
        assert stations[3].name in routes[0].get_way()

    def test_route_delete_intermediate_station(self, routes, stations):
        routes[0].delete_intermediate_station(stations[3])
        assert stations[3] not in routes[0].get_way()

    def test_route_delete_intermediate_station_not_found(self, routes, stations):
        assert 'No station were found' in routes[0].delete_intermediate_station(stations[3])

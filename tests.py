import pytest
from main import Station, Train, Route


class BaseSetUp:

    @pytest.fixture(scope='session')
    def stations(self):
        return [
            Station('Kyiv'),
            Station('Lviv'),
            Station('Yalta'),
            Station('Przemysl')
        ]


    @pytest.fixture(scope='session')
    def trains(self):
        return [
            Train(200, 'passenger', 5),
            Train(300, 'passenger', 3),
            Train(400, 'cargo', 9),
            Train(500, 'cargo', 15)
        ]

    @pytest.fixture(scope='session')
    def routes(self, stations):
        return [
            Route(stations[0], stations[1]),
            Route(stations[1], stations[0]),
            Route(stations[0], stations[2]),
        ]


class TestRoute(BaseSetUp):

    def test_route_repr(self, routes):
        expected_repr = "Route(start=Station(name='Kyiv'), end=Station(name='Yalta'))"
        assert repr(routes[2]) == expected_repr

    def test_route_way(self, routes):
        assert routes[2].way == []

    def test_route_get_way(self, routes, stations):
        assert 'Kyiv', 'Yalta' in routes[2].get_way()
    def test_route_add_way(self, routes, stations):
        routes[0].add_intermediate_station(stations[3])
        assert stations[3] in routes[0].way

    def test_route_delete_intermediate_station(self, routes, stations):
        routes[0].delete_intermediate_station(stations[3])
        assert stations[3] not in routes[0].way

    def test_route_delete_intermediate_station_not_found(self, routes, stations):
        assert 'No station were found' in routes[0].delete_intermediate_station(stations[3])


class TestTrain(BaseSetUp):

    def test_train_repr(self, trains):
        expected_repr = "Train(number=200, train_type='passenger', wagons_amount=5)"
        assert repr(trains[0]) == expected_repr

    def test_train_speed_zero(self, trains):
        assert trains[0].speed == 0

    def test_train_gain_speed(self, trains):
        trains[0].gain_speed()
        assert trains[0].speed == 10

    def test_train_get_speed(self, trains):
        assert trains[0].get_speed() == 'The current speed of the train is 10 km/h.'

    def test_train_brake(self, trains):
        trains[0].brake()
        assert trains[0].speed == 0

    def test_train_wagons_amount(self, trains):
        assert trains[0].get_wagons_amount() == 5

    def test_train_add_wagon(self, trains):
        trains[0].add_wagon()
        assert trains[0].wagons_amount == 6

    def test_train_remove_wagon(self, trains):
        trains[0].remove_wagon()
        assert trains[0].wagons_amount == 5

    def test_train_add_wagon_with_speed(self, trains):
        trains[0].gain_speed()
        assert trains[0].add_wagon() == 'The current speed of the train is 10 km/h. Please, stop first.'

    def test_train_remove_wagon_with_speed(self, trains):
        trains[0].gain_speed()
        assert trains[0].remove_wagon() == 'The current speed of the train is 20 km/h. Please, stop first.'

    def test_train_no_route(self, trains):
        assert trains[0].get_train_stops() == 'Train has no route'
    def test_train_add_route(self, trains, routes):
        assert trains[0].add_route(routes[0]) == ['Kyiv', 'Lviv']

    def test_train_get_stops(self, trains):
        assert trains[0].get_train_stops() == 'Current station: Kyiv\nPrevious station: -\nNext station: Lviv'

    def test_train_get_3_stops(self, trains, routes, stations):
        routes[0].add_intermediate_station(stations[2])
        assert trains[0].get_train_stops() == 'Current station: Kyiv\nPrevious station: -\nNext station: Yalta'

    def test_train_move_to_the_first(self, trains, routes):
        assert trains[0].move_to_previous_station() == 'Train is already at the first station.'

    def test_train_move_to_next_station(self, trains):
        trains[0].move_to_next_station()
        assert trains[0].get_train_stops() == 'Current station: Yalta\nPrevious station: Kyiv\nNext station: Lviv'

    def test_train_move_to_the_end(self, trains, routes):
        trains[0].move_to_next_station()
        assert trains[0].get_train_stops() == 'Current station: Lviv\nPrevious station: Yalta\nNext station: -'

    def test_train_move_to_the_end_again(self, trains, routes):
        assert trains[0].move_to_next_station() == 'Train is already at the last station.'

    def test_train_move_to_the_previous_station(self, trains, routes):
        assert trains[0].move_to_previous_station() == 'Train moved to Yalta'

class TestStation(BaseSetUp):

    def test_station_repr(self, stations):
        expected_repr = "Station(name='Kyiv')"
        assert repr(stations[0]) == expected_repr

    def test_get_trains_all(self, stations):
        assert stations[0].get_trains() == []

    def test_get_trains_filtered_passenger(self, stations, trains):
        stations[0].add_train(trains[0])
        stations[0].add_train(trains[1])
        assert stations[0].get_trains('passenger') == [trains[0], trains[1]]

    def test_get_trains_filtered_cargo(self, stations, trains):
        stations[0].add_train(trains[2])
        assert stations[0].get_trains('cargo') == [trains[2]]

    def test_add_train(self, stations, trains):
        stations[0].add_train(trains[3])
        assert trains[3] in stations[0].get_trains()

    def test_departure_train(self, stations, trains):
        stations[0].departure_train(trains[3])
        assert trains[3] not in stations[0].get_trains()

    def test_departure_train_not_found(self, stations, trains):
        assert 'No train at the station were found' in stations[0].departure_train(trains[3])

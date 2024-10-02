import pytest
from railway.route import Route
from railway.train import Train, PassengerTrain, CargoTrain
from railway.station import Station
from railway.wagon import CargoWagon, PassengerWagon

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
    def train(self):
        return [
            Train(1)
        ]

    @pytest.fixture(scope='session')
    def passenger_trains(self):
        return [
            PassengerTrain(200),
            PassengerTrain(300),
            PassengerTrain(400),
            PassengerTrain(500)
        ]

    @pytest.fixture(scope='session')
    def cargo_trains(self):
        return [
            CargoTrain(200),
            CargoTrain(300),
            CargoTrain(400),
            CargoTrain(500)
        ]

    @pytest.fixture(scope='session')
    def passenger_wagons(self):
        return [
            PassengerWagon(1, 15),
            PassengerWagon(2, 50),
            PassengerWagon(3, 100),
            PassengerWagon(4, 200),
        ]

    @pytest.fixture(scope='session')
    def cargo_wagons(self):
        return [
            CargoWagon(1, 500),
            CargoWagon(2, 50),
            CargoWagon(3, 150),
            CargoWagon(4, 1000)
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


class TestTrain(BaseSetUp):

    def test_train_NotImplementedError(self, train, passenger_wagons):
        with pytest.raises(NotImplementedError):
            train[0].add_wagon(passenger_wagons[0])


class TestPassengerTrain(BaseSetUp):

    def test_pass_train_repr(self, passenger_trains):
        expected_repr = "PassengerTrain(number=200)"
        assert repr(passenger_trains[0]) == expected_repr

    def test_pass_train_get_all_instances(self, passenger_trains, train):
        assert passenger_trains[0].all() == {1: train[0],
                                            200: passenger_trains[0],
                                            300: passenger_trains[1],
                                            400: passenger_trains[2],
                                            500: passenger_trains[3]
                                            }

    def test_pass_train_gain_speed(self, passenger_trains):
        passenger_trains[0].gain_speed(25)
        assert passenger_trains[0].get_speed() == 'The current speed of the train is 25 km/h.'

    def test_pass_train_brake(self, passenger_trains):
        passenger_trains[0].brake()
        assert passenger_trains[0]._speed == 0

    def test_pass_train_wagons_amount(self, passenger_trains):
        assert passenger_trains[0].get_wagons_amount() == 0

    def test_pass_train_add_wagon(self, passenger_trains, passenger_wagons):
        passenger_trains[0].add_wagon(passenger_wagons[0])
        assert passenger_trains[0].get_wagons_amount() == 1

    def test_pass_train_add_cargo_wagon(self, passenger_trains, cargo_wagons):
        assert "Invalid wagon type for this train." in passenger_trains[0].add_wagon(cargo_wagons[0])

    def test_pass_train_remove_wagon(self, passenger_trains, passenger_wagons):
        passenger_trains[0].remove_wagon(passenger_wagons[0])
        assert passenger_trains[0].get_wagons_amount() == 0

    def test_pass_train_add_wagon_with_speed(self, passenger_trains, passenger_wagons):
        passenger_trains[0].gain_speed(250)
        assert passenger_trains[0].add_wagon(passenger_wagons[0]) == ('The current speed of the train is 250 km/h. '
                                                                    'Please, stop first.')

    def test_pass_train_remove_wagon_with_speed(self, passenger_trains, passenger_wagons):
        passenger_trains[0].gain_speed(250)
        assert passenger_trains[0].remove_wagon(passenger_wagons[0]) == ('The current speed of the train is 500 km/h. '
                                                                        'Please, stop first.')

    def test_pass_train_no_route(self, passenger_trains):
        assert passenger_trains[0].get_train_stops() == 'Train has no route'


    def test_pass_train_add_route(self, passenger_trains, routes):
        assert passenger_trains[0].add_route(routes[0]) == ['Kyiv', 'Lviv']

    def test_pass_train_get_stops(self, passenger_trains):
        assert passenger_trains[0].get_train_stops() == 'Current station: Kyiv\nPrevious station: -\nNext station: Lviv'

    def test_pass_train_get_3_stops(self, passenger_trains, routes, stations):
        routes[0].add_intermediate_station(stations[2])
        assert passenger_trains[0].get_train_stops() == 'Current station: Kyiv\nPrevious station: -\nNext station: Yalta'

    def test_pass_train_move_to_the_first(self, passenger_trains, routes):
        assert passenger_trains[0].move_to_previous_station() == 'Train is already at the first station.'

    def test_pass_train_move_to_next_station(self, passenger_trains):
        passenger_trains[0].move_to_next_station()
        assert passenger_trains[0].get_train_stops() == 'Current station: Yalta\nPrevious station: Kyiv\nNext station: Lviv'

    def test_pass_train_move_to_the_end(self, passenger_trains, routes):
        passenger_trains[0].move_to_next_station()
        assert passenger_trains[0].get_train_stops() == 'Current station: Lviv\nPrevious station: Yalta\nNext station: -'

    def test_pass_train_move_to_the_end_again(self, passenger_trains, routes):
        assert passenger_trains[0].move_to_next_station() == 'Train is already at the last station.'

    def test_pass_train_move_to_the_previous_station(self, passenger_trains, routes):
        assert passenger_trains[0].move_to_previous_station() == 'Train moved to Yalta'


class TestCargoTrain(BaseSetUp):
    """Without repeated tests from the passenger train"""

    def test_cargo_train_repr(self, cargo_trains):
        expected_repr = "CargoTrain(number=200)"
        assert repr(cargo_trains[0]) == expected_repr

    def test_cargo_train_add_pass_wagon(self, cargo_trains, passenger_wagons):
        assert "Invalid wagon type for this train." in cargo_trains[0].add_wagon(passenger_wagons[0])


class TestStation(BaseSetUp):

    def test_station_repr(self, stations):
        expected_repr = "Station(name='Kyiv')"
        assert repr(stations[0]) == expected_repr

    def test_station_get_trains_all(self, stations):
        assert stations[0].get_trains() == []

    def test_station_add_trains(self, stations, passenger_trains, cargo_trains):
        assert stations[0].add_train(passenger_trains[0]) == [passenger_trains[0]]
        assert stations[0].add_train(cargo_trains[0]) == [passenger_trains[0], cargo_trains[0]]

    def test_station_get_all_instances(self, stations):
        assert stations[0].all() == {'Kyiv': stations[0],
                                    'Lviv': stations[1],
                                    'Yalta': stations[2],
                                    'Przemysl': stations[3]
                                    }

    def test_station_add_train(self, stations, train):
        assert stations[0].add_train(train[0]) == 'Only passenger or cargo trains allowed'

    def test_station_get_trains_filtered(self, stations, passenger_trains, cargo_trains):
        assert stations[0].get_trains('passenger') == [passenger_trains[0]]
        assert stations[0].get_trains('cargo') == [cargo_trains[0]]
        assert stations[0].get_trains('largo') == 'Wrong filter'

    def test_station_departure_train_subclass(self, stations, passenger_trains):
        stations[0].departure_train(passenger_trains[0])
        assert passenger_trains[0] not in stations[0].get_trains()

    def test_station_departure_train_not_found(self, stations, passenger_trains):
        assert 'No train at the station were found' in stations[0].departure_train(passenger_trains[0])

    def test_station_departure_train(self, stations, train):
        assert stations[0].add_train(train[0]) == 'Only passenger or cargo trains allowed'

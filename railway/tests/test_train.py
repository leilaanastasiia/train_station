import pytest
from railway.tests.test_data import BaseSetUp
from railway.train import PassengerTrain


class TestTrain(BaseSetUp):

    def test_train_NotImplementedError(self, train, passenger_wagons):
        with pytest.raises(NotImplementedError):
            train[0].add_wagon(passenger_wagons[0])


class TestPassengerTrain(BaseSetUp):

    def test_pass_train_get_all_instances(self, passenger_trains, train):
        assert passenger_trains[0].all() == {1: train[0],
                                            200: passenger_trains[0],
                                            300: passenger_trains[1],
                                            400: passenger_trains[2],
                                            500: passenger_trains[3]
                                            }

    def test_pass_train_instances_decorator(self, passenger_trains):
        assert passenger_trains[0].instances() == 8
        station = PassengerTrain(555)
        assert station.instances() == 9

    def test_pass_train_repr(self, passenger_trains):
        expected_repr = "PassengerTrain(number=200)"
        assert repr(passenger_trains[0]) == expected_repr

    def test_pass_train_find(self, passenger_trains):
        assert passenger_trains[0].find(200) == passenger_trains[0]
        assert passenger_trains[0].find(900) is None

    def test_pass_train_manufacturers(self, passenger_trains):
        assert passenger_trains[0].get_manufacturer() == 'Product has no manufacturer.'
        assert passenger_trains[0].add_manufacturer('Python') == 'Python'
        assert passenger_trains[0].delete_manufacturer() is None

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


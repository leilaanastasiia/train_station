import pytest

from railway.station import Station
from railway.tests.test_data import BaseSetUp


class TestStation(BaseSetUp):

    def test_station_get_all_instances(self, stations):
        assert stations[0].all() == {'Kyiv': stations[0],
                                    'Lviv': stations[1],
                                    'Yalta': stations[2],
                                    'Przemysl': stations[3]
                                    }

    def test_station_instances_decorator(self, stations):
        assert stations[0].instances() == 8
        station = Station('Dnipro')
        assert station.instances() == 9

    def test_station_is_valid(self):
        assert Station('qwerty').name == 'Qwerty'

    def test_station_is_not_valid(self):
        with pytest.raises(ValueError, match="Station's name must be a string."):
            Station(120)

    def test_station_repr(self, stations):
        expected_repr = "Station(name='Kyiv')"
        assert repr(stations[0]) == expected_repr

    def test_station_get_trains_all(self, stations):
        assert stations[0].get_trains() == []

    def test_station_add_trains(self, stations, passenger_trains, cargo_trains):
        assert stations[0].add_train(passenger_trains[0]) == [passenger_trains[0]]
        assert stations[0].add_train(cargo_trains[0]) == [passenger_trains[0], cargo_trains[0]]

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

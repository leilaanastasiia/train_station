import pytest
from railway.route import Route
from railway.station import Station
from railway.train import Train, PassengerTrain, CargoTrain
from railway.wagon import PassengerWagon, CargoWagon


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
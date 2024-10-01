from __future__ import annotations
from railway.train import Train, PassengerTrain, CargoTrain
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .train import PassengerTrain, CargoTrain


class Station:
    """
    Represents a station class.
    """

    def __init__(self, name):
        self.name = name
        self._trains = []

    def get_trains(self, train_filter=None):
        if not train_filter:
            return self._trains
        elif train_filter == 'passenger':
            return [train for train in self._trains if isinstance(train, PassengerTrain)]
        elif train_filter == 'cargo':
            return [train for train in self._trains if isinstance(train, CargoTrain)]

    def add_train(self, train: PassengerTrain|CargoTrain) -> list|str:
        if not issubclass(Train, type(train)):
            self._trains.append(train)
            return self._trains
        else:
            return 'Only passenger or cargo trains allowed'

    def departure_train(self, train: PassengerTrain|CargoTrain):
        try:
            if not issubclass(Train, type(train)):
                self._trains.remove(train)
                return self._trains
            else:
                return 'Only passenger or cargo trains allowed'
        except ValueError as ve:
            return f'No train at the station were found: {ve}.'

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(name={self.name!r})"
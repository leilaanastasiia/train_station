from __future__ import annotations
from railway.train import Train, PassengerTrain, CargoTrain
from railway.decorators import instance_counter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .train import PassengerTrain, CargoTrain


@instance_counter
class Station:
    """
    Represents a station class.
    """
    instances_dict = {}

    def __init__(self, name):
        if self._is_valid(name):
            self.name = name.capitalize()
            self._trains = []
            Station.instances_dict[self.name] = self
        else:
            raise ValueError("Station's name must be a string.")

    @staticmethod
    def all():
        return Station.instances_dict

    @staticmethod
    def _is_valid(name):
        if isinstance(name, str) and len(name) > 0:
            return name
        else:
            return None

    def get_trains(self, train_filter=None):
        if not train_filter:
            return self._trains
        elif train_filter == 'passenger':
            return [train for train in self._trains if isinstance(train, PassengerTrain)]
        elif train_filter == 'cargo':
            return [train for train in self._trains if isinstance(train, CargoTrain)]
        else:
            return 'Wrong filter'

    def call_trains(self, func):
        if not callable(func):
            raise TypeError('The function must be callable.')
        else:
            for train in self._trains:
                return func(train)

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

    def __str__(self):
        return self.name

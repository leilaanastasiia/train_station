from __future__ import annotations
from railway.wagon import PassengerWagon, CargoWagon
from railway.manufacturer import Manufacturer
from railway.decorators import instance_counter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .route import Route


class Train(Manufacturer):
    """
    Represents a train class.
    """
    instances = {}

    def __init__(self, number, manufacturer_name=None):
        super().__init__()
        self.number = number
        self.manufacturer_name = manufacturer_name
        Train.instances[self.number] = self
        """
        Private attributes bellow because it is better do not have an accesses the them directly
        for an unexpected behavior.
        """
        self._speed = 0
        self._wagons = []
        self._current_route = None
        self._current_station_index = None

    @staticmethod
    def all():
        return Train.instances

    @staticmethod
    def find(number):
        try:
            train = Train.instances[number]
            return train
        except KeyError:
            return None

    def gain_speed(self, speed):
        self._speed += speed
        return self._speed

    def brake(self):
        self._speed = 0
        return self._speed

    def get_speed(self):
        return f'The current speed of the train is {self._speed} km/h.'

    def get_wagons_amount(self):
        return len(self._wagons)

    def get_wagons(self):
        return self._wagons

    def _validate_wagon_type(self, wagon: PassengerWagon|CargoWagon):
        """
        Must be implemented in subclasses. Direct access is highly undesired :)
        """
        raise NotImplementedError()

    def add_wagon(self, wagon: PassengerWagon|CargoWagon):
        if self._validate_wagon_type(wagon):
            if self._speed == 0:
                self._wagons.append(wagon)
                return self._wagons
            else:
                return f'The current speed of the train is {self._speed} km/h. Please, stop first.'
        else:
            return "Invalid wagon type for this train."

    def remove_wagon(self, wagon: PassengerWagon|CargoWagon):
        if self._speed == 0:
            try:
                self._wagons.remove(wagon)
                return self._wagons
            except ValueError as ve:
                return f'No wagon were found: {ve}.'
        else:
            return f'The current speed of the train is {self._speed} km/h. Please, stop first.'

    def add_route(self, route: Route):
        self._current_route = route
        self._current_station_index = 0
        return self._current_route.get_way()

    def get_train_stops(self):
        if self._current_route:
            way = self._current_route.get_way()
            current_station = way[self._current_station_index]
            previous_station = None if self._current_station_index == 0 else way[self._current_station_index - 1]
            next_station = None if self._current_station_index == len(way) - 1 else way[self._current_station_index + 1]
            return (f"Current station: {current_station}\n"
                    f"Previous station: {'-' if previous_station is None else previous_station}\n"
                    f"Next station: {'-' if next_station is None else next_station}")
        else:
            return 'Train has no route'

    def move_to_next_station(self):
        if self._current_route and self._current_station_index < len(self._current_route.get_way()) - 1:
            self._current_station_index += 1
            return f"Train moved to {self._current_route.get_way()[self._current_station_index]}"
        else:
            return "Train is already at the last station."

    def move_to_previous_station(self):
        if self._current_route and self._current_station_index > 0:
            self._current_station_index -= 1
            return f"Train moved to {self._current_route.get_way()[self._current_station_index]}"
        else:
            return "Train is already at the first station."

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r})"


@instance_counter
class PassengerTrain(Train):
    """
    Represents a passenger train class.
    """
    def _validate_wagon_type(self, wagon: PassengerWagon):
        return isinstance(wagon, PassengerWagon)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r})"


@instance_counter
class CargoTrain(Train):
    """
    Represents a cargo train class.
    """
    def _validate_wagon_type(self, wagon: CargoWagon):
        return isinstance(wagon, CargoWagon)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r})"

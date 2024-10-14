from railway.manufacturer import Manufacturer
from railway.decorators import validate_number, validate_wagon_subclass


class Wagon(Manufacturer):
    """
    Represents a wagon class.
    """

    @validate_number
    def __init__(self, number, manufacturer_name=None):
        super().__init__(manufacturer_name)
        self.number = number

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r})"


class PassengerWagon(Wagon):
    """
    Represents a passenger wagon class.
    """

    @validate_wagon_subclass
    def __init__(self, number, capacity, manufacturer_name=None):
        super().__init__(number, manufacturer_name)
        self.capacity = capacity
        self.total_capacity = self.capacity

    def take_seat(self):
        if self.capacity > 0:
            self.capacity -= 1
            return self.capacity
        raise ValueError('All seats are taken.')

    def taken_seats(self):
        return self.total_capacity - self.capacity

    def free_seats(self):
        return self.capacity

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r}, capacity={self.capacity!r})"


class CargoWagon(Wagon):
    """
    Represents a cargo wagon class.
    """
    @validate_wagon_subclass
    def __init__(self, number, max_weight, manufacturer_name=None):
        super().__init__(number, manufacturer_name)
        self.max_weight = max_weight
        self.weight_left = max_weight

    def load_weight(self, kg):
        if self.weight_left - kg >= 0:
            self.weight_left -= kg
            return self.weight_left
        raise ValueError("Wagon's max weight is exceeded.")

    def taken_weight(self):
        return self.max_weight - self.weight_left

    def free_weight(self):
        return self.weight_left

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r}, max_weight={self.max_weight!r})"

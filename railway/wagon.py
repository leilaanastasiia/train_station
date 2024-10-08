from railway.manufacturer import Manufacturer


class Wagon(Manufacturer):
    """
    Represents a wagon class.
    """
    def __init__(self, number, manufacturer_name=None):
        super().__init__()
        self.manufacturer_name = manufacturer_name
        if self._is_valid(number):
            self.number = number
        else:
            raise ValueError("Wagon's number must be an integer.")

    @staticmethod
    def _is_valid(number):
        if isinstance(number, int):
            return number
        return None

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(number={self.number!r})"

class PassengerWagon(Wagon):
    """
    Represents a passenger wagon class.
    """

    def __init__(self, number, capacity, manufacturer_name=None):
        super().__init__(number)
        self.manufacturer_name = manufacturer_name
        if self._is_valid(capacity):
            self.capacity = capacity
            self.total_capacity = self.capacity
        else:
            raise ValueError("Wagon's capacity must be an integer.")

    @staticmethod
    def _is_valid(capacity):
        if isinstance(capacity, int):
            return capacity
        return None

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

    def __init__(self, number, max_weight, manufacturer_name=None):
        super().__init__(number)
        self.manufacturer_name = manufacturer_name
        if self._is_valid(max_weight):
            self.max_weight = max_weight
            self.weight_left = max_weight
        else:
            raise ValueError("Wagon's max weight must be an integer.")

    @staticmethod
    def _is_valid(max_weight):
        if isinstance(max_weight, int):
            return max_weight
        return None

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

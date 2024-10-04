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
        else:
            return None

class PassengerWagon(Wagon):
    """
    Represents a passenger wagon class.
    """

    def __init__(self, number, capacity, manufacturer_name=None):
        super().__init__(number)
        self.manufacturer_name = manufacturer_name
        if self._is_valid(capacity):
            self.capacity = capacity
        else:
            raise ValueError("Wagon's capacity must be an integer.")

    @staticmethod
    def _is_valid(capacity):
        if isinstance(capacity, int):
            return capacity
        else:
            return None

class CargoWagon(Wagon):
    """
    Represents a cargo wagon class.
    """

    def __init__(self, number, max_weight, manufacturer_name=None):
        super().__init__(number)
        self.manufacturer_name = manufacturer_name
        if self._is_valid(max_weight):
            self.max_weight = max_weight
        else:
            raise ValueError("Wagon's max weight must be an integer.")

    @staticmethod
    def _is_valid(max_weight):
        if isinstance(max_weight, int):
            return max_weight
        else:
            return None
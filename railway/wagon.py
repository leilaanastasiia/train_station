from railway.manufacturer import Manufacturer


class Wagon(Manufacturer):
    """
    Represents a wagon class.
    """
    
    def __init__(self, number, manufacturer_name=None):
        super().__init__()
        self.number = number
        self.manufacturer_name = manufacturer_name


class PassengerWagon(Wagon):
    """
    Represents a passenger wagon class.
    """

    def __init__(self, number, capacity, manufacturer_name=None):
        super().__init__(number)
        self.capacity = capacity
        self.manufacturer_name = manufacturer_name

class CargoWagon(Wagon):
    """
    Represents a cargo wagon class.
    """

    def __init__(self, number, max_weight, manufacturer_name=None):
        super().__init__(number)
        self.max_weight = max_weight
        self.manufacturer_name = manufacturer_name

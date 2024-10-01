class Wagon:
    """
    Represents a wagon class.
    """
    
    def __init__(self, number):
        self.number = number


class PassengerWagon(Wagon):
    """
    Represents a passenger wagon class.
    """

    def __init__(self, number, capacity):
        super().__init__(number)
        self.capacity = capacity

class CargoWagon(Wagon):
    """
    Represents a cargo wagon class.
    """

    def __init__(self, number, max_weight):
        super().__init__(number)
        self.max_weight = max_weight
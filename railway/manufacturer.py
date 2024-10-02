class Manufacturer:
    """
    Represents a manufacturer class.
    """

    def __init__(self):
        self.manufacturer_name = None

    def add_manufacturer(self, manufacturer_name):
        self.manufacturer_name = manufacturer_name
        return self.manufacturer_name

    def get_manufacturer(self):
        if self.manufacturer_name:
            return self.manufacturer_name
        else:
            return 'Product has no manufacturer.'

    def delete_manufacturer(self):
        self.manufacturer_name = None
        return self.manufacturer_name
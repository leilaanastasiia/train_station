class Manufacturer:
    """
    Represents a manufacturer class.
    """

    def __init__(self):
        self.manufacturer_name = None

    @staticmethod
    def is_valid(manufacturer_name):
        if isinstance(manufacturer_name, str) and len(manufacturer_name) > 0:
            return manufacturer_name
        return None

    def add_manufacturer(self, manufacturer_name: str):
        if self.is_valid(manufacturer_name):
            self.manufacturer_name = manufacturer_name
            return self.manufacturer_name
        raise ValueError("Manufacturer's name must be a string.")

    def get_manufacturer(self):
        if self.manufacturer_name:
            return self.manufacturer_name
        return 'Product has no manufacturer.'

    def delete_manufacturer(self):
        self.manufacturer_name = None
        return self.manufacturer_name

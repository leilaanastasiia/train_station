from railway.decorators import validate_manufacturer


class Manufacturer:
    """
    Represents a manufacturer class.
    """
    @validate_manufacturer
    def __init__(self, manufacturer_name=None):
        self.manufacturer_name = manufacturer_name

    @validate_manufacturer
    def add_manufacturer(self, manufacturer_name: str):
        self.manufacturer_name = manufacturer_name
        return self.manufacturer_name

    def get_manufacturer(self):
        if self.manufacturer_name:
            return self.manufacturer_name
        return 'Product has no manufacturer.'

    def delete_manufacturer(self):
        self.manufacturer_name = None
        return self.manufacturer_name

import pytest

from railway.manufacturer import Manufacturer


class TestManufacturer:

    def test_manufacturer_init(self):
        assert Manufacturer()
        assert Manufacturer('Tornado')

    def test_manufacturer_init_err_number(self):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            Manufacturer(1)

    def test_manufacturer_init_err_str(self):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            Manufacturer('')

    def test_manufacturer_add_get_delete(self):
        manufacturer = Manufacturer()
        assert manufacturer.get_manufacturer() == 'Product has no manufacturer.'
        assert manufacturer.add_manufacturer('Pipi') == 'Pipi'
        assert manufacturer.get_manufacturer() == 'Pipi'
        assert manufacturer.delete_manufacturer() is None

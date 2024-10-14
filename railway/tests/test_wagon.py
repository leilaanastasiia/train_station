import pytest

from railway.tests.test_data import BaseSetUp
from railway.wagon import PassengerWagon, CargoWagon, Wagon


class TestWagon:

    def test_wagon(self):
        expected_repr = "Wagon(number=1)"
        wagon = Wagon(1)
        assert wagon.number == 1
        assert repr(wagon) == expected_repr
        assert Wagon(1, None)
        assert Wagon(1, '1')

    def test_wagon_err_number(self):
        with pytest.raises(ValueError, match='Invalid number.'):
            assert Wagon('1')

    def test_wagon_err_manufacturer(self):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            assert Wagon(1, 1)


class TestPassWagons(BaseSetUp):

    def test_pass_wagon_manufacturer(self):
        assert PassengerWagon(1,1)
        assert PassengerWagon(1, 1, 'Name')
    def test_pass_wagon_number_error(self):
        with pytest.raises(ValueError, match="Invalid number."):
            PassengerWagon('h', 8)

    def test_pass_wagon_capacity_error(self):
        with pytest.raises(ValueError, match="Invalid capacity|weight."):
            PassengerWagon(44, 'r')

    def test_pass_wagon_manufacturer_error(self):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            PassengerWagon(44, 44, 9)

    def test_pass_wagon_get_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].get_manufacturer() == 'Product has no manufacturer.'
        assert PassengerWagon(2, 5, 'Python').get_manufacturer() == 'Python'

    def test_pass_wagon_add_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].add_manufacturer('Python') == 'Python'

    def test_pass_wagon_add_manufacturer_error_number(self, passenger_wagons):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            passenger_wagons[0].add_manufacturer(12)

    def test_pass_wagon_add_manufacturer_error_empty_str(self, passenger_wagons):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            passenger_wagons[0].add_manufacturer('')

    def test_pass_wagon_delete_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].delete_manufacturer() is None

    def test_pass_wagon_seats(self, passenger_wagons):
        assert passenger_wagons[0].take_seat() == 3
        assert passenger_wagons[0].take_seat() == 2
        assert passenger_wagons[0].take_seat() == 1
        assert passenger_wagons[0].take_seat() == 0
        assert passenger_wagons[0].taken_seats() == 4
        assert passenger_wagons[0].free_seats() == 0

    def test_pass_wagon_take_seat_error(self, passenger_wagons):
        with pytest.raises(ValueError, match='All seats are taken.'):
            passenger_wagons[0].take_seat()

class TestCargoWagons(BaseSetUp):

    def test_cargo_wagon_manufacturer(self):
        assert CargoWagon(1,1)
        assert CargoWagon(1, 1, 'Name')
    def test_cargo_wagon_number_error(self):
        with pytest.raises(ValueError, match="Invalid number."):
            CargoWagon('h', 8)

    def test_cargo_wagon_capacity_error(self):
        with pytest.raises(ValueError, match="Invalid capacity|weight."):
            CargoWagon(44, 'r')

    def test_cargo_wagon_manufacturer_error(self):
        with pytest.raises(ValueError, match="Manufacturer's name must be a string."):
            CargoWagon(44, 44, 9)

    def test_cargo_wagon_max_weight_error(self):
        with pytest.raises(ValueError, match="Invalid capacity|weight."):
            CargoWagon(44, 'r')

    def test_cargo_wagon_weight(self, cargo_wagons):
        assert cargo_wagons[0].load_weight(200) == 300
        assert cargo_wagons[0].load_weight(100) == 200
        assert cargo_wagons[0].taken_weight() == 300
        assert cargo_wagons[0].free_weight() == 200

    def test_cargo_wagon_take_weight_error(self, cargo_wagons):
        with pytest.raises(ValueError, match="Wagon's max weight is exceeded."):
            cargo_wagons[0].load_weight(1000)

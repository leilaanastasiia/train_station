from railway.tests.test_data import BaseSetUp


class TestWagons(BaseSetUp):

    def test_pass_wagon_get_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].get_manufacturer() == 'Product has no manufacturer.'

    def test_pass_wagon_add_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].add_manufacturer('Python') == 'Python'

    def test_pass_wagon_delete_manufacturer(self, passenger_wagons):
        assert passenger_wagons[0].delete_manufacturer() is None

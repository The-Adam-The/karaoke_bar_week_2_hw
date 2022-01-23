import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):

        #drinks
        self.asahi = Drink("Asahi Dry", "Beer", 300)


    def test_drink_has_name(self):
        self.assertEqual("Asahi Dry", self.asahi.name)

    def test_drink_has_type(self):
        self.assertEqual("Beer", self.asahi.drink_type)

    def test_drink_has_price(self):
        self.assertEqual(300, self.asahi.price)


 
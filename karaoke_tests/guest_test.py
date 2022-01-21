import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.tanaka = Guest("Tanaka", 23, 30000)
        self.morita = Guest("Morita", 17, 34000)

    def test_guest_name(self):
        self.assertEqual("Tanaka", self.tanaka.name)

    def test_guest_age(self):
        self.assertEqual(23, self.tanaka.age)

    def test_guest_can_order_alchohol(self):
        self.assertEqual(True, self.tanaka.can_order_alcohol())

    def test_guest_can_not_order_alchohol(self):
        self.assertEqual(False, self.morita.can_order_alcohol())
    
    def test_guest_has_money(self):
        self.assertEqual(30000, self.tanaka.money)

    
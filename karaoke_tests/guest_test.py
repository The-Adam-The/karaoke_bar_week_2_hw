import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.tanaka = Guest("Tanaka")

    def test_guest_name(self):
        self.assertEqual("Tanaka", self.tanaka.name)

        

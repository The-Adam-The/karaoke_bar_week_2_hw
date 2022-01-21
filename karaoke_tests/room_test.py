import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.tomomi = Guest("Tomomi", 28)
        self.honda = Guest("Honda", 43)
        self.tanaka = Guest("Tanaka", 23)
        self.room1 = Room(1, 8, [])
        self.room2 = Room(2, 6, [self.tomomi])
        self.room3  = Room(3, 10, [self.tomomi, self.honda, self.tanaka])
        

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_num)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room1.capacity)

    def test_room_current_occupancy(self):
        self.assertEqual([self.tomomi], self.room2.current_occupancy)

    def test_room_available(self):
        self.assertEqual("Room 1 available.", self.room1.check_room_availability())

    def test_room_unavailable(self):
        self.assertEqual("Room 2 unavailable.", self.room2.check_room_availability())

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.honda)
        self.assertEqual([self.honda], self.room1.current_occupancy)

    def test_check_in_multiple_guests(self):
        self.room1.check_in_guest(self.honda, self.tomomi)
        self.assertEqual([self.honda, self.tomomi], self.room1.current_occupancy)

    def test_check_out_guest(self):
        self.room3.check_out_guest(self.honda)
        self.assertEqual([self.tomomi, self.tanaka], self.room3.current_occupancy)

    def test_check_out_guests(self):
        self.room3.check_out_guest(self.honda, self.tomomi)
        self.assertEqual([self.tanaka], self.room3.current_occupancy)

    def test_check_out_all_guests(self):
        self.room3.check_out_all_guests()
        self.assertEqual([], self.room3.current_occupancy)

    
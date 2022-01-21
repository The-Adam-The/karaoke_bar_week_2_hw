import unittest
from classes.room import Room

class RoomTest(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room(1, 8, [])
        self.room2 = Room(2, 6, ["test"])

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_num)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room1.capacity)

    def test_room_current_occupancy(self):
        self.assertEqual([], self.room1.current_occupancy)

    def test_room_available(self):
        self.assertEqual("Room 1 available.", self.room1.check_room_availability())

    def test_room_unavailable(self):
        self.assertEqual("Room 2 unavailable.", self.room2.check_room_availability())
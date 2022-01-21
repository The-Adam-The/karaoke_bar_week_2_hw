import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.tomomi = Guest("Tomomi", 28, 439900)
        self.honda = Guest("Honda", 43, 209900)
        self.tanaka = Guest("Tanaka", 23, 200390)
        self.yoshida = Guest("Yoshida", 31, 200499)
        self.david = Guest("David", 29, 499000)
        self.sarah = Guest("Sarah", 23, 249095)
        self.hashimoto = Guest("Hashimoto", 30, 348987)

        self.plastic_love = Song("Plastic Love", "Mariya Takeuchi", "City Pop")
        self.master_of_puppets = Song("Master of Puppets", "Metallica", "Metal")
        self.dancing_queen = Song("Dancing Queen", "Abba", "Pop")
        self.stayin_alive = Song("Stayin' Alive", "BeeGees", "Disco")


        self.room1 = Room(1, 6, [], [self.plastic_love, self.dancing_queen,])
        self.room2 = Room(2, 6, [self.tomomi], [self.master_of_puppets])
        self.room3  = Room(3, 10, [self.tomomi, self.honda, self.tanaka], [self.stayin_alive])
        
        

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.room_num)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room1.capacity)

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

    def test_check_in_too_many_guests(self):
        self.assertEqual("Only 8 people are able to use this room. Please choose a larger room.", self.room1.check_in_guest(self.tomomi, self.honda, self.tanaka, self.david, self.sarah, self.yoshida, self.hashimoto))

    def test_check_out_guest(self):
        self.room3.check_out_guest(self.honda)
        self.assertEqual([self.tomomi, self.tanaka], self.room3.current_occupancy)

    def test_check_out_guests(self):
        self.room3.check_out_guest(self.honda, self.tomomi)
        self.assertEqual([self.tanaka], self.room3.current_occupancy)

    def test_check_out_all_guests(self):
        self.room3.check_out_all_guests()
        self.assertEqual([], self.room3.current_occupancy)

    def test_room_has_song_list(self):
        self.assertEqual([self.stayin_alive], self.room3.song_list)
    
    
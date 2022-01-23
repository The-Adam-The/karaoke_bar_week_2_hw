import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    
    def setUp(self):

        #guests
        self.tomomi = Guest("Tomomi", 28, 439900, "Stayin' Alive")
        self.honda = Guest("Honda", 43, 209900, "Guile Theme")
        self.tanaka = Guest("Tanaka", 23, 200390, "Hotel California")
        self.yoshida = Guest("Yoshida", 31, 200500, "Smells like Teen Spirit")
        self.david = Guest("David", 29, 499000, "The Impossible Dream")
        self.sarah = Guest("Sarah", 23, 300, "Combine Harvester")
        self.hashimoto = Guest("Hashimoto", 30, 348987, "Jailhouse Rock")
        self.ginko = Guest("Ginko", 32, 200, "Scrub")

        #songs
        self.plastic_love = Song("Plastic Love", "Mariya Takeuchi", "City Pop")
        self.master_of_puppets = Song("Master of Puppets", "Metallica", "Metal")
        self.dancing_queen = Song("Dancing Queen", "Abba", "Pop")
        self.stayin_alive = Song("Stayin' Alive", "BeeGees", "Disco")

        #drinks
        self.asahi_dry = Drink("Asahi Dry", "Beer", 300)
        self.smirnoff = Drink("Smirnoff", "Vodka", 250)
        self.zero = Drink("Zero-Orange", "Alcopop", 100)
        self.pinot = Drink("Pinot Noir", "Red Wine", 350)
        self.nihonshyuu = Drink("Nihonshyuu", "Sake", 400)
        self.orange = Drink("Orange Juice", "Mixer", 100)
        self.coke = Drink("Coca Cola", "Mixer", 100)
        self.water = Drink("Water", "Water", 0)

        #rooms
        self.room1 = Room(1, 6, [], [self.plastic_love, self.dancing_queen], [self.smirnoff])
        self.room2 = Room(2, 6, [self.tomomi], [self.master_of_puppets], [self.nihonshyuu, self.nihonshyuu, self.coke, self.nihonshyuu, self.coke, 
        self.asahi_dry, self.smirnoff, self.asahi_dry, self.smirnoff, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry])
        self.room3  = Room(3, 10, [self.tomomi, self.honda, self.tanaka], [self.stayin_alive], [])
        
        

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
    
    def test_entry_fee(self):
        self.assertEqual(500, self.room1.entry_fee)

    def test_customer_has_sufficient_funds(self):
        self.assertEqual(True, self.room1.customer_has_sufficient_funds(self.david.money))

    def test_customer_has_insufficient_funds(self):
        self.assertEqual(False, self.room1.customer_has_sufficient_funds(self.sarah.money))

    def test_pay_entry_fee(self):
        self.room1.pay_entry_fee(self.yoshida)
        self.assertEqual(200000, self.yoshida.money)

    def test_check_in_guest_denied_entry(self):
        self.assertEqual("The following guests have insufficient funds: Sarah Ginko" ,self.room1.check_in_guest(self.sarah, self.ginko ))

    def test_room_has_bar_tab(self):
        self.assertEqual([self.smirnoff], self.room1.bar_tab)

     #Is there a way to test if a statement has been printed?

    # def test_guest_responds_to_favorite_song(self):
    #     self.assertEqual("Honda: かこい! Guile Theme! この曲が大好きだ! 歌いたい!", self.room1.favorite_song_react(self.honda.name, "Guile Theme"))

    # def test_guest_responds_to_favorite_song_in_room(self):
    #     self.assertEqual("Tomomi: かこい! Stayin' Alive! この曲が大好きだ! 歌いたい!", self.room3.check_in_guest(self.tomomi))
       
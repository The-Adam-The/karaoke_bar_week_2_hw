import unittest
from classes.bar import Bar
from classes.drink import Drink
from classes.guest import Guest
from classes.room import Room

class TestBar(unittest.TestCase):

    def setUp(self):
        #drinks
        self.asahi_dry = Drink("Asahi Dry", "Beer", 300)
        self.smirnoff = Drink("Smirnoff", "Vodka", 250)
        self.zero = Drink("Zero-Orange", "Alcopop", 100)
        self.pinot = Drink("Pinot Noir", "Red Wine", 350)
        self.nihonshyuu = Drink("Nihonshyuu", "Sake", 400)
        self.orange = Drink("Orange Juice", "Mixer", 100)
        self.coke = Drink("Coca Cola", "Mixer", 100)
        self.water = Drink("Water", "Water", 0)

        #guests
        self.tomomi = Guest("Tomomi", 28, 439900, "Stayin' Alive")
        self.paulo = Guest("Paulo", 9, 2000, "Baby Shark")

        #bar
        self.main_bar = Bar("Main Bar", 20000, [self.asahi_dry, self.smirnoff, self.zero, self.pinot, self.nihonshyuu, self.orange, self.coke, self.water])
        
        #rooms
        self.room2 = Room(2, 6, [self.tomomi], [], [self.nihonshyuu, self.nihonshyuu, self.coke, self.nihonshyuu, self.coke, 
        self.asahi_dry, self.smirnoff, self.asahi_dry, self.smirnoff, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry])


       

    def test_bar_has_name(self):
        self.assertEqual("Main Bar", self.main_bar.name)
    
    def test_bar_has_till(self):
        self.assertEqual(20000, self.main_bar.till)

    def test_bar_has_drink_list(self):
        self.assertEqual([self.asahi_dry, self.smirnoff, self.zero, self.pinot, self.nihonshyuu, self.orange, self.coke, self.water], self.main_bar.drink_list)

    def test_add_money_to_till(self):
        self.main_bar.add_money_to_till(100)
        self.assertEqual(20100, self.main_bar.till)

    def test_guest_can_buy_alcohol(self):
        self.assertEqual(True, self.main_bar.guest_can_buy_alcohol(self.tomomi.age))

    def test_guest_can_not_buy_alcohol(self):
        self.assertEqual(False, self.main_bar.guest_can_buy_alcohol(self.paulo.age))

    def test_room_calc_large_bar_tab(self):
        self.assertEqual(4600, self.main_bar.calc_bar_tab(self.room2.room_num, self.room2.bar_tab))

    def test_room_order_drink(self):
        self.room2.order_drink(self.asahi_dry)
        self.assertEqual([self.nihonshyuu, self.nihonshyuu, self.coke, self.nihonshyuu, self.coke, 
        self.asahi_dry, self.smirnoff, self.asahi_dry, self.smirnoff, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry, self.asahi_dry], self.room2.bar_tab)

    def test_guest_can_afford_bar_tab(self):
        self.assertEqual(True, self.main_bar.guest_has_sufficient_funds(self.tomomi.money, 4600))

    def test_clear_bar_tab(self):
        self.main_bar.clear_bar_tab(self.room2)
        self.assertEqual([], self.room2.bar_tab)

    def test_guest_pay_bar_tab(self):
        self.main_bar.guest_pay_bar_tab(self.tomomi, self.room2)
        self.assertEqual([], self.room2.bar_tab)

    def test_guest_can_not_pay_bar_tab(self):
        self.assertEqual("Guest: Paulo has insufficient funds.", self.main_bar.guest_pay_bar_tab(self.paulo, self.room2) )



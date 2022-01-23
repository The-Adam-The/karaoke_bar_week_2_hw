class Bar:
    def __init__(self, name, till, drink_list):
        self.name = name
        self.till = till
        self.drink_list = drink_list
        

    def add_money_to_till(self, money):
        self.till += money

    def guest_can_buy_alcohol(self, guest_age):
        if guest_age >= 18:
            return True
        return False

    def calc_bar_tab(self, room_num, bar_tab):
        total_bill = 0
        for drink in bar_tab:
            total_bill += drink.price
        print(f"Room {room_num}'s bill: ¥{total_bill}")
        return total_bill

    def guest_has_sufficient_funds(self, guest_money, bar_tab):
        if guest_money >= bar_tab:
            return True
        return False

    def clear_bar_tab(self, room):
        room.bar_tab.clear()


    def guest_pay_bar_tab(self, guest, room):
        bill = self.calc_bar_tab(room.room_num, room.bar_tab)
        if self.guest_has_sufficient_funds(guest.money, bill):
           self.add_money_to_till(bill)
           self.clear_bar_tab(room)
           guest.pay_money(bill)

        else:
            return f"Guest: {guest.name} has insufficient funds."

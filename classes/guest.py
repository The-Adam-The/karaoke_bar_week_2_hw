class Guest:

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def can_order_alcohol(self):
        if self.age >= 18:
            return True
        return False

    
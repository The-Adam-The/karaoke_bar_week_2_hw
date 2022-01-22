class Guest:

    def __init__(self, name, age, money, favorite_song):
        self.name = name
        self.age = age
        self.money = money
        self.favorite_song = favorite_song
        
    def can_order_alcohol(self):
        if self.age >= 18:
            return True
        return False

    
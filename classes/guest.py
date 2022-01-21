class Guest:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_order_alcohol(self):
        if self.age >= 18:
            return True
        return False

        
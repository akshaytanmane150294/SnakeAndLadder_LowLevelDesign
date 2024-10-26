import random


class Dice():
    def __init__(self, sides):
        self.sides = sides

    def get_value(self):
        return random.randint(1, self.sides)

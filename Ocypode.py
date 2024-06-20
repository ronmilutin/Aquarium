import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width=7
    def get_animal(self):
        return [[" ", "*", " ", " ", " ", "*", " "],[" ", " ", "*", "*", "*", " ", " "],["*", "*", "*", "*", "*", "*", "*"],["*", " ", " ", " ", " ", " ", "*"]]


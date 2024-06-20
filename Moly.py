import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)


    def get_animal(self):
        if self.directionH == 0:
            return [[" ", "*", "*", "*", " ", " ", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"],
         [" ", "*", "*", "*", " ", " ", "*", "*"]]
        elif self.directionH == 1:
            return [["*", "*", " ", " ", "*", "*", "*", " "], ["*", "*", "*", "*", "*", "*", "*", "*"],
                    ["*", "*", " ", " ", "*", "*", "*", " "]]

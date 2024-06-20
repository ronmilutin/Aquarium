import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7




    def get_animal(self):
        if self.directionH==0:
            return [["*"," ","*"," "," "," "," "],[" ","*","*","*","*","*","*"],[" "," ","*"," ","*"," "," "]]
        elif self.directionH==1:
            return [[" "," "," "," ","*"," ","*"],["*","*","*","*","*","*"," "],[" "," ","*"," ","*"," "," "]]







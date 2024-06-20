import Animal


MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)



    def __str__(self):
        pass

    def starvation(self):
        print("The crab " + self.name + " died an the age of " + str(self.age) + " years because he ran out of food" )


    def die(self):
        print(self.name + " died in good health")

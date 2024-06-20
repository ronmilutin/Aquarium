MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120
FEED_AMOUNT = 10


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        pass

    def get_food(self):
        return self.food

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def dec_food(self):
        self.food -= 1

    def inc_age(self):
        self.age += 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def get_position(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x=x

    def set_y(self, y):
        self.y=y

    def starvation(self):
        pass

    def die(self):
        pass

    def get_directionH(self):
        return self.directionH

    def set_directionH(self, directionH):
        if directionH == 1:
            self.directionH = 0
        else:
            self.directionH = 1


    def get_alive(self):
        if self.get_age()!=0:
            return True
            

    def get_size(self):
        pass

    def get_food_amount(self):
        return self.food

    def add_food(self, amount=0):
        self.food += FEED_AMOUNT

    def get_animal(self):
        pass
from typing import Any, Union

from Animal import Animal
from Fish import Fish
from Crab import Crab
from Shrimp import Shrimp
from Scalar import Scalar
from Moly import Moly
from Ocypode import Ocypode


MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []

    def build_tank(self):
        self.board = []
        for i in range (self.aqua_height):
            current_row=[]
            for j in range (self.aqua_width):
                if i==self.aqua_height-1:
                    if j==0:
                        current_row += ['\\']
                    elif j==self.aqua_width-1:
                        current_row += ['/']
                    else:
                        current_row += ['_']
                elif j == 0 or j==self.aqua_width-1:
                    current_row+=['|']
                elif i == WATERLINE-1:
                    current_row += ['~']
                else:
                    current_row += [' ']
            self.board.append(current_row)



    def print_board(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print("")
    def get_board(self):
        return self.board

    def get_all_animal(self):
        return self.anim

    def is_collision(self, animal):
        for i in self.anim:
            if isinstance(i, Crab):
                if animal.get_directionH()==0 and i.get_directionH()==1:
                    if animal.x==i.x+i.width:
                        i.set_directionH(i.get_directionH())
                        animal.set_directionH(animal.get_directionH())
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
                        if animal.get_directionH() == 1:
                            self.right(animal)
                        else:
                            self.left(animal)
                        return True
                    if animal.x==i.x+i.width+1:
                        i.set_directionH(i.get_directionH())
                        animal.set_directionH(animal.get_directionH())
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
                        if animal.get_directionH() == 1:
                            self.right(animal)
                        else:
                            self.left(animal)
                        return True
                if animal.get_directionH()==1 and i.get_directionH()==0:
                    if animal.x + animal.width == i.x:
                        i.set_directionH(i.get_directionH())
                        animal.set_directionH(animal.get_directionH())
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
                        if animal.get_directionH() == 1:
                            self.right(animal)
                        else:
                            self.left(animal)
                        return True
                    if animal.x + animal.width+1 == i.x:
                        i.set_directionH(i.get_directionH())
                        animal.set_directionH(animal.get_directionH())
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
                        if animal.get_directionH() == 1:
                            self.right(animal)
                        else:
                            self.left(animal)
                        return True
        return False

    def print_animal_on_board(self, animal: Animal):
        x = animal.x
        y = animal.y
        pattern=animal.get_animal()
        for i in range(y,y+len(pattern)):
            for j in range(x,x+len(pattern[i-y])):
                if pattern[i-y][j-x] == '*':
                    self.board[i][j] = pattern[i-y][j-x]


    def delete_animal_from_board(self, animal: Animal):
        x = animal.x
        y = animal.y
        pattern = animal.get_animal()
        for i in range(y, y + len(pattern)):
            for j in range(x, x + len(pattern[i - y])):

                self.board[i][j] = " "

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        if fishtype == "mo":
            moly = Moly(name, age, x, y, directionH, directionV)
            self.anim.append(moly)
            if moly.x>self.aqua_width-9:
                moly.x = self.aqua_width-9
            if moly.y > self.aqua_height - MAX_CRAB_HEIGHT-4:
                moly.y = self.aqua_height - MAX_CRAB_HEIGHT-4
            a = self.check_if_free(moly.x,moly.y)
            if a:
                self.print_animal_on_board(moly)
                return True
            else:
                self.anim.remove(moly)
                return False
        elif fishtype == "sc":
            scalar = Scalar(name, age, x, y, directionH, directionV)
            self.anim.append(scalar)
            if scalar.x > self.aqua_width - 9:
                scalar.x = self.aqua_width - 9
            if scalar.y > self.aqua_height-MAX_CRAB_HEIGHT-MAX_FISH_HEIGHT-1:
                scalar.y = self.aqua_height-MAX_CRAB_HEIGHT-MAX_FISH_HEIGHT-1
            a = self.check_if_free(scalar.x, scalar.y)
            if a:
                self.print_animal_on_board(scalar)
                return True
            else:
                self.anim.remove(scalar)
                return False

    def add_crab(self, name, age, x, y, directionH, crabtype):
        if crabtype == "sh":
            newy = len(self.board) - 4
            shrimp = Shrimp(name, age, x, newy, directionH)
            self.anim.append(shrimp)
            if shrimp.x>self.aqua_width-8:
                shrimp.x = self.aqua_width-8
            a = self.check_if_free(shrimp.x, y)
            if a:
                self.print_animal_on_board(shrimp)
                return True
            else:
                self.anim.remove(shrimp)
                return False

        elif crabtype == "oc":
            newy = len(self.board) - 5
            ocypode = Ocypode(name, age, x, newy, directionH)
            self.anim.append(ocypode)
            if ocypode.x > self.aqua_width - 8:
                ocypode.x = self.aqua_width - 8
            a = self.check_if_free(ocypode.x, y)
            if a:
                self.print_animal_on_board(ocypode)
                return True
            else:
                self.anim.remove(ocypode)
                return False

    def check_if_free(self, x, y) -> bool:
        check_last = self.anim[-1]
        if isinstance(check_last, Fish):
            for i in range(5):
                for j in range (MAX_ANIMAL_WIDTH):
                    if self.board[y+i][x+j] == "*":
                        print("The place is not available! Please try again later.")
                        return False
            return True
        else:
            for i in range(4):
                for j in range(MAX_ANIMAL_WIDTH):
                    if self.board[y-1-i][x+j] == "*":
                        print("The place is not available! Please try again later.")
                        return False
            return True


    def left(self, a):
        if a.get_directionH() == 0:
            self.delete_animal_from_board(a)
            for j in self.anim:
                if isinstance(j, Fish):
                     if j != a:
                        self.print_animal_on_board(j)
            a.left()
            self.print_animal_on_board(a)


    def right(self, a):
        if a.get_directionH()==1:
            self.delete_animal_from_board(a)
            for j in self.anim:
                if isinstance(j, Fish):
                    if j != a:
                        self.print_animal_on_board(j)
            a.right()
            self.print_animal_on_board(a)

    def up(self, a):
        if isinstance(a, Fish):
            if a.get_directionV() == 1:
                self.delete_animal_from_board(a)
                for j in self.anim:
                    if isinstance(j,Fish):
                        if j!=a:
                            self.print_animal_on_board(j)
                a.up()
                self.print_animal_on_board(a)

    def down(self, a):
        if isinstance(a,Fish):
            if a.get_directionV()==0:
                self.delete_animal_from_board(a)
                for j in self.anim:
                    if isinstance(j,Fish):
                        if j!=a:
                            self.print_animal_on_board(j)
                a.down()
                self.print_animal_on_board(a)

    def next_turn(self):
        self.turn += 1
        collides_at_first = True
        for i in self.anim:
            if self.turn%10 == 1 or self.turn == 1:
                i.dec_food()
            if self.turn%100 == 0:
                i.inc_age()
            side_edge = True
            upper_edge = True
            if i.get_x() == 1 and i.get_directionH()==0:
                self.delete_animal_from_board(i)
                i.set_directionH(i.get_directionH())
                self.print_animal_on_board(i)
                side_edge = False
            if isinstance(i, Shrimp) or isinstance(i, Ocypode):
                if i.get_x() == self.aqua_width-8 and i.get_directionH()==1:
                    self.delete_animal_from_board(i)
                    i.set_directionH(i.get_directionH())
                    self.print_animal_on_board(i)
                    side_edge = False
            if isinstance(i, Fish):
                if i.get_x() == self.aqua_width-9 and i.get_directionH()==1:
                    i.set_directionH(i.get_directionH())
                    side_edge = False
            if isinstance(i, Scalar):
                needs_to_go_up = i.get_y() == self.aqua_height - MAX_CRAB_HEIGHT-MAX_FISH_HEIGHT-1 and i.get_directionV()==0
                needs_to_go_down = i.get_y() == 3 and i.get_directionV() == 1
                if needs_to_go_up or needs_to_go_down:
                    i.set_directionV(i.get_directionV())
                    upper_edge = False
            if isinstance(i, Moly):
                needs_to_go_up = i.get_y() == self.aqua_height - MAX_CRAB_HEIGHT-4 and i.get_directionV()==0
                needs_to_go_down = i.get_y() == 3 and i.get_directionV() == 1
                if needs_to_go_up or needs_to_go_down:
                    i.set_directionV(i.get_directionV())
                    upper_edge = False
            collides = False
            if isinstance(i, Crab):
                if collides_at_first:
                    if self.is_collision(i):
                        collides = True
            if isinstance(i, Fish):
                if side_edge:
                    if not collides:
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
            if isinstance(i, Crab):
                if side_edge:
                    if not collides:
                        if i.get_directionH() == 1:
                            self.right(i)
                        else:
                            self.left(i)
                        collides_at_first = False
            if isinstance(i, Shrimp) or isinstance(i, Ocypode):
                upper_edge = False
            if upper_edge:
                if i.get_directionV() == 1:
                    self.up(i)
                else:
                    self.down(i)
            if i.get_age() == 120:
                i.die()
                self.anim.remove(i)
                self.delete_animal_from_board(i)
            if i.get_food_amount() == 0:
                i.starvation()
                self.anim.remove(i)
                self.delete_animal_from_board(i)

    def print_all(self):
        for i in self.anim:
            if isinstance(i, Fish):
                print("The fish " + i.get_name() + " is " + str(i.get_age())
                      + " years old and with " + str(i.get_food_amount()) + " food")
            else:
                print("The crab " + i.get_name() + " is "
                      + str(i.get_age()) + " years old and with " + str(i.get_food_amount()) + " food")


    def feed_all(self):
        for i in self.anim:
            i.add_food()

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        try:
            num_of_turns = (int(input("how many steps do you want to take?")))
            for i in range(num_of_turns):
                self.next_turn()
        except ValueError:
            print("Please enter an integer")




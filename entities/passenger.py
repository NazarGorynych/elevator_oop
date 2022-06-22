from random import randint


class Passenger:
    """
    Upon initialization accepts floor_number aas current floor at which passenger is. Also, accepts house as
    instance of class House from which it can get randomized amount of total_floor. Passenger then uses this parameter
    to determine range in which it can randomize floor to get to. At last, it chooses direction where to move.
    """
    def __init__(self, floor_number: int, house):
        self.pressed_button = None
        self.desired_floor = None
        self.at_floor = floor_number
        self.house = house
        self.get_desired_floor()
        self.press_button()

    # randomizes desired floor so that it's not the same as current floor of the resident
    def get_desired_floor(self):
        self.desired_floor = randint(1, self.house.total_floors)
        while self.at_floor == self.desired_floor:
            self.desired_floor = randint(1, self.house.total_floors)
        return self.desired_floor

    # chooses direction (True or False) based on current floor and needed floor
    def press_button(self):
        self.pressed_button = True if self.desired_floor > self.at_floor else False

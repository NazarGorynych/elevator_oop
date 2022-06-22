from random import randint
from entities.passenger import Passenger


class Floor:
    """
    Generates random number of instances of Passenger. Gives as arguments it's floor number
    and house instance where it all belongs to.
    """
    def __init__(self, floor_number: int, house):
        self.floor_number = floor_number
        self.residents = []
        self.total_residents = randint(0, 10)
        self.house = house
        self.__generate_passengers()

    def __generate_passengers(self):
        for resident in range(self.total_residents):
            self.residents.append(Passenger(floor_number=self.floor_number, house=self.house))
from entities.floor import Floor


class House:
    """
    House instance that excepts generated random total_floors based on which
    it creates instances of Floor given amount of total_floors.
    """
    def __init__(self, total_floors: int):
        self.total_floors = total_floors
        self.floors = []
        self.__generate_floor()

    # assign each new floor a number
    def __generate_floor(self):
        for step in range(1, self.total_floors+1):
            floor = Floor(floor_number=step, house=self)
            self.floors.append(floor)

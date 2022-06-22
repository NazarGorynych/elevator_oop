from entities.passenger import Passenger


class Elevator:
    """
    Working instance of class Elevator which accommodates up to 5 residents (by turning them into passengers),
    then moves them to maximum floor that passengers have. During ascension/descension drops people at floors
    if they match their desired_floors. If the elevator has less than 5 residents it will stop on its way and take
    more, then reevaluate maximum or minimum floors again.
    """
    def __init__(self, house):
        self.passengers = []
        self.ascending = None
        self.current_position = 1  # initial position
        self.floor_to_reach = 2
        self.house = house
        self.desired_floors = []

    # boarding passengers regarding their chosen direction and current direction of the elevator
    def board_passengers(self):
        for resident in self.__get_floor().residents:
            if self.floor_to_reach > self.current_position:
                if resident.pressed_button:
                    self.resident_enter_elevator(resident)
            elif self.floor_to_reach < self.current_position:
                if not resident.pressed_button:
                    self.resident_enter_elevator(resident)

    # elevator limit check, transfer from resident to passenger
    def resident_enter_elevator(self, resident: Passenger):
        if len(self.passengers) < 5:
            self.passengers.append(resident)
            self.__get_floor().residents.remove(resident)
            print(f'Resident with desired floor #{resident.desired_floor} embarked at'
                  f' floor #{self.__get_floor().floor_number}')

    # get desired floor of each passenger
    def get_desired_floors(self):
        self.desired_floors = [i.desired_floor for i in self.passengers]

    # iterate over list of passengers to disembark at floor if needed
    def disembark_passengers(self):
        to_disembark = [x for x in self.passengers if x.desired_floor == self.current_position]
        for passenger in to_disembark:
            passenger.at_floor = self.current_position
            print(f'Passenger with desired floor number {passenger.desired_floor} has disembarked'
                  f' at floor #{self.__get_floor().floor_number}')
            self.__get_floor().residents.append(passenger)
            self.passengers.remove(passenger)
            passenger.get_desired_floor()
            passenger.press_button()

    # sets direction in ascending --- True = UP, False = DOWN
    def set_direction(self):
        if self.floor_to_reach > self.current_position or self.current_position == 1:
            self.ascending = True
            self.floor_to_reach = self.house.total_floors if not self.desired_floors else max(self.desired_floors)
        else:
            self.ascending = False
            self.floor_to_reach = 1 if not self.desired_floors else min(self.desired_floors)

    # algorythm of actions
    def move(self):
        print(f' - - - STEP - - -\n')
        self.board_passengers()
        self.get_desired_floors()
        self.set_direction()
        print(f'Desired floors by passengers: {self.desired_floors}')
        self.current_position += 1 if self.ascending else - 1
        self.disembark_passengers()

        # printing information
        print(f'Current floor: {self.current_position}')
        print(f'Floor to reach: {self.floor_to_reach}')
        print('Direction UP') if self.ascending else print('Direction DOWN')
        print(f'\n- - - END - - - ')

    # gets current floor instance from house.floors list
    # based on index that matches current position of the elevator
    def __get_floor(self):
        return self.house.floors[self.current_position - 1]  # - 1  to fix IndexOutOfRange

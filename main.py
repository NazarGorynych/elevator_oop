# -----------------------------------------------------------
# This is a rather simple elevator model implemented in OOP style in Python3
# The project follows given algorythm to transport random individuals
# between randomly generated amount of floors. The resident must push the button
# to instruct the system which way he/she needs to go. The limit of the passengers in
# the elevator is 5. Once passenger reached desired floor, he chooses another one.
#  If the elevator is not full, it will stop to get more people.
#
# (C) 2022 Horchytsia Nazarii, Khmelnytskyi, Ukraine
# Email: horchytsia.nazarii@gmail.com
# -----------------------------------------------------------


from random import randint


class House:
    floors = []
    total_floors = randint(5, 20)

    def __init__(self):
        step = 0
        # assign each new floor a number
        for count in range(self.total_floors):
            step += 1
            floor = Floor(floor_number=step)
            self.floors.append(floor)


class Elevator:
    passengers = []
    ascending = None
    current_position = 1  # initial position
    floor_to_reach = 2

    # boarding passengers regarding their chosen direction and current direction of the elevator
    def board_passengers(self):
        for resident in list(House.floors[self.current_position - 1].residents):
            if self.floor_to_reach > self.current_position:
                if resident.pressed_button:
                    self.resident_enter_elevator(resident)
            elif self.floor_to_reach < self.current_position:
                if not resident.pressed_button:
                    self.resident_enter_elevator(resident)

    # elevator limit check, transfer from resident to passenger
    def resident_enter_elevator(self, resident):
        if len(self.passengers) < 5:
            self.passengers.append(resident)
            House.floors[self.current_position - 1].residents.remove(resident)
            print(f'Resident with desired floor #{resident.desired_floor} embarked at'
                  f' floor #{House.floors[self.current_position - 1].floor_number}')

    # get desired floor of each passenger
    def get_desired_floors(self):
        self.desired_floors = []
        for passenger in self.passengers:
            self.desired_floors.append(passenger.desired_floor)

    # iterate over list of passengers to disembark at floor if needed
    def disembark_passengers(self):
        for passenger in list(self.passengers):
            if passenger.desired_floor == self.current_position:
                passenger.at_floor = self.current_position
                print(f'Passenger with desired floor number {passenger.desired_floor} has disembarked'
                      f' at floor #{House.floors[self.current_position - 1].floor_number}')
                House.floors[self.current_position - 1].residents.append(passenger)
                self.passengers.remove(passenger)
                passenger.get_desired_floor()
                passenger.press_button()

    # algorythm of actions
    def move(self):
        print(f' - - - STEP - - -\n')
        self.board_passengers()
        self.get_desired_floors()
        self.set_direction()
        print(f'Desired floors by passengers: {self.desired_floors}')
        if self.ascending:
            self.current_position += 1
        else:
            self.current_position -= 1
        self.disembark_passengers()

        # printing information
        print(f'Current floor: {self.current_position}')
        print(f'Floor to reach: {self.floor_to_reach}')
        if self.ascending:
            print('Direction: UP')
        else:
            print('Direction: DOWN')
        print(f'\n- - - END - - - ')

    # sets direction in ascending --- True = UP, False = DOWN
    def set_direction(self):
        if self.floor_to_reach > self.current_position or self.current_position == 1:
            self.ascending = True
            try:
                self.floor_to_reach = max(self.desired_floors)
            except ValueError:
                self.floor_to_reach = House.total_floors
        else:
            self.ascending = False
            try:
                self.floor_to_reach = min(self.desired_floors)
            except ValueError:
                self.floor_to_reach = 1


class Passenger:
    pressed_button = None
    desired_floor = None

    def __init__(self, floor_number):
        self.at_floor = floor_number
        self.get_desired_floor()
        self.press_button()

    # randomizes desired floor so that it's not the same as current floor of the resident
    def get_desired_floor(self):
        self.desired_floor = randint(1, House.total_floors)
        while self.at_floor == self.desired_floor:
            self.desired_floor = randint(1, House.total_floors)
        return self.desired_floor

    # chooses direction of desired floor
    def press_button(self):
        if self.desired_floor > self.at_floor:
            self.pressed_button = True
        else:
            self.pressed_button = False


class Floor:

    def __init__(self, floor_number):
        self.floor_number = floor_number    # get generated floor number from House
        self.residents = []
        self.total_residents = randint(0, 10)
        for resident in range(self.total_residents):   # generate passengers
            self.residents.append(Passenger(floor_number))


def main():
    House()
    elevator = Elevator()
    print(f'Total floors: {House.total_floors}')
    for i in range(100):
        elevator.move()


main()

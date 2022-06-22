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
from entities.elevator import Elevator
from entities.house import House


def main():
    total_floors = randint(5, 20)
    house = House(total_floors)
    elevator = Elevator(house)

    print(f'Total floors: {house.total_floors}')
    for i in range(100):
        elevator.move()


if __name__ == '__main__':
    main()

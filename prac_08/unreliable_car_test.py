
from prac_08.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Good", 100, 100)
    unreliable_car = UnreliableCar("Bad", 100, 9)

    for i in range(1, 10):
        print("Attempting to drive {}km:".format(i))
        print("{} drove {}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{} drove {}km".format(unreliable_car.name, unreliable_car.drive(i)))

    print(reliable_car)
    print(unreliable_car)


main()

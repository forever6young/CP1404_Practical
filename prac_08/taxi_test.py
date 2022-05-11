from prac_08.taxi import Taxi


def main():
    taxi_information = Taxi('Prius 1', 100, 1.23)
    taxi_information.drive(40)
    print(taxi_information)
    taxi_information.start_fare()
    taxi_information.drive(100)
    print(taxi_information)


main()

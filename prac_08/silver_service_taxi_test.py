from prac_08.silver_service_taxi import SilverServiceTaxi


def main():

    taxi = SilverServiceTaxi("Test Silver ServiceTaxi", 100, 6)
    taxi.drive(36)
    print(taxi)
    print(taxi.get_fare())


main()

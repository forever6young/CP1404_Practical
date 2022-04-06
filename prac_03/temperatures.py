"""
CP1404 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """  
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
    """
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c2f(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f2c(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def f2c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def c2f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()

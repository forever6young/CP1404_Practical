
import random

A_lines_numbers = 6
Min = 1
Max = 45


def main():
    pick_times = int(input("How many quick picks? "))
    for i in range(pick_times):
        quick_picks = []
        for j in range(A_lines_numbers):
            number = random.randint(Min, Max)
            while number in quick_picks:
                number = random.randint(Min, Max)
            quick_picks.append(number)
        quick_picks.sort()
        print(quick_picks)


main()

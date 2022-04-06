"""
CP1404 - Practical
Broken program to determine score status
"""

from random import randrange


def main():
    score = float(input("Enter score: "))
    result = score_result(score)
    print(result)
    result = score_result(randrange(100))
    print(result)


def score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 50:
            return "Passable"
        if score > 90:
            return "Excellent"
    if score < 50:
        return "Bad"


if __name__ == '__main__':
    main()


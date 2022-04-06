try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")

"""Questions
1.When will a ValueError occur?
2.When will a ZeroDivisionError occur?
3.Could you change the code to avoid the possibility of a ZeroDivisionError?"""
# 1.When the numerator or denominator I input is not a number but a letter or other symbol
# 2.Denominator is 0
# 3.(Done above)

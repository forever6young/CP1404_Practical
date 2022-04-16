"""
CP1404 Practical
State names in a dictionary
File needs reformatting
15/04/2022 done
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for key, value in CODE_TO_NAME.items():
    print('{:<3} is {}'.format(key, value))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

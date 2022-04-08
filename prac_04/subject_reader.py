"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def main():
    details = get_data()
    show_subjects(details)


def get_data():
    details = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        detail = [parts[0], parts[1], parts[2]]
        details.append(detail)
    input_file.close()
    return details


def show_subjects(details):
    for detail in details:
        print(f"{detail[0]} is taught by {detail[1]:12} and has {detail[2]:3} students")


main()

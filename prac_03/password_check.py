"""
Description: A simple Password Check

Name: Zhaoyang Wang
"""


def main():
    password = get_password()
    if check_length(password):
        print_asterisk(password)
    else:
        print("password check not passed")


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("Input the password: ")
    return password


def check_length(password):
    min_length = 6
    return len(password) >= min_length


if __name__ == '__main__':
    main()

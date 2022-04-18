def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        question = input("Is your name {}? (Y/n) ".format(name))
        if question.upper() != "Y" and question != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    raw_data = email.split('@')[0]
    data = raw_data.split('.')
    name = " ".join(data).title()
    return name


main()

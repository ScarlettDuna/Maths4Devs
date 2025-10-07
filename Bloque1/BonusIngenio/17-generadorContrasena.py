import string
import random

def pass_gen():
    options = ["yes", "no"]
    password = ""
    # ask for the number of characters the password should contain
    while True:
        pass_length = input("How long do you want the password? Insert a number between 8 and 15: ")
        try:
            pass_length = int(pass_length)
            if 8 <= pass_length <= 15:
                break
            else:
                print("Error! Insert only a number between 8 and 15.")
        except ValueError:
            print("Error! Please insert a valid number.")
    # ask if it has capital letters
    has_capitals = input("Should the password contain capital letters? Insert 'yes' or 'no'. ")
    while has_capitals.strip().lower() not in options:
        has_capitals = input(" Insert only 'yes' or 'no'. ")
    # ask if it has numbers
    has_numbers = input("Should the password contain numbers? Insert 'yes' or 'no'. ")
    while has_numbers.strip().lower() not in options:
        has_numbers = input(" Insert only 'yes' or 'no'. ")
    # ask if it has symbols
    has_symbols = input("Should the password contain symbols? Insert 'yes' or 'no'. ")
    while has_symbols.strip().lower() not in options:
        has_symbols = input(" Insert only 'yes' or 'no'. ")

    # Generate list of options (types of characters)
    char_options = [list(string.ascii_lowercase)]
    if has_capitals.strip().lower() == "yes":
        char_options.append(list(string.ascii_uppercase))
    if has_numbers.strip().lower() == "yes":
        char_options.append(list(string.digits))
    if has_symbols.strip().lower() == "yes":
        char_options.append(list("!@#$%^&*()-_=+;:,.<>?"))

    # making sure at least one char of each type is included in the password
    password_chars = []
    for charset in char_options:
        password_chars.append(random.choice(charset))

    remaining_length = pass_length - len(password_chars)
    # create list with al the char available
    all_chars = [ch for charset in char_options for ch in charset]
    password_chars.extend(random.choices(all_chars, k=remaining_length))
    random.shuffle(password_chars)
    password = ''.join(password_chars)


    print("Generated password: " + password)
    return password

password_1 = pass_gen()
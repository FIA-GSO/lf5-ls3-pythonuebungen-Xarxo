import time

from rich.console import Console
from random import randint

console = Console()


def validate_input(prompt, error_message, validator, string_true="", string_false="", int_range=[]):
    while True:
        try:
            if validator == str:
                user_input = validator(console.input(prompt))
                user_input = user_input.lower()

                if string_true == "" and string_false == "":
                    return user_input

                if user_input == string_true:
                    return user_input
                elif user_input == string_false:
                    return user_input
                else:
                    continue
            else:
                user_input = validator(input(prompt))
                if int_range == []:
                    return user_input
                elif int_range != [] and (user_input < int_range[0] or user_input > int_range[1]):
                    continue
                else:
                    return user_input
        except ValueError:
            print(error_message)


def get_player_range():
    if number_of_matches < 7:
        return [1, number_of_matches]
    else:
        return [1, 6]


def player_turn(_number_of_matches):
    player_range = get_player_range()

    number_of_player_matches = validate_input("Wie viele Streichhölzer ziehen Sie (min. 1 & max. 6): ",
                                              "Geben Sie eine Zahl zwischen 1 bis 6 an!", int,
                                              "", "", player_range)
    _number_of_matches -= number_of_player_matches

    return _number_of_matches


def check_last_match():
    if number_of_matches == 1:
        console.clear()
        print("Du hast Gewonnen, Glückwunsch")
        time.sleep(2)


def check_zero_match():
    if number_of_matches == 0:
        print("Du hast leider verloren :(")


def computer_turn(_number_of_matches):
    number_of_bot_matches = randint(1, 6)
    while number_of_bot_matches > _number_of_matches or number_of_bot_matches == _number_of_matches:
        number_of_bot_matches = randint(1, _number_of_matches - 1)

    print("Der Computer zieht " + str(number_of_bot_matches) + " Streichhölzer.")
    time.sleep(2)

    _number_of_matches -= number_of_bot_matches

    return _number_of_matches


number_of_matches = 0

print("Willkommen zum Nim-Spiel (Streichholzspiel) \n")

starting_player = validate_input("Wählen Sie aus wer das Spiel beginnt. "
                                 "\nGeben Sie \"A\" ein damit der Computer startet. "
                                 "Und \"B\" damit Sie starten: ", "Geben Sie bitte \"A\", oder \"B\" ein.",
                                 str, "a", "b")

if starting_player == "a":
    number_of_matches = randint(7, 31)
    print("Es gibt " + str(number_of_matches) + " Streichhölzer dieses Spiel.")
    time.sleep(3)
elif starting_player == "b":
    number_of_matches = validate_input("Geben Sie die Anzahl der zu ziehenden Streichhölzer an (min. 7): ",
                                       "Geben Sie eine Zahl ein!", int, "", "", [7, 999])

while number_of_matches > 0:
    if starting_player == "a":
        if check_last_match():
            break

        number_of_matches = computer_turn(number_of_matches)

        print("\n\n" + str(number_of_matches) + " Streichhölzer übrig!!")
        time.sleep(2)
        console.clear()

        number_of_matches = player_turn(number_of_matches)

        if check_zero_match():
            break

        print("\n\n" + str(number_of_matches) + " Streichhölzer übrig!!")
        time.sleep(2)
        console.clear()
    else:
        number_of_matches = player_turn(number_of_matches)

        if check_zero_match():
            break

        print("\n\n" + str(number_of_matches) + " Streichhölzer übrig!!")
        time.sleep(2)
        console.clear()

        if check_last_match():
            break

        number_of_matches = computer_turn(number_of_matches)

        print("\n\n" + str(number_of_matches) + " Streichhölzer übrig!!")
        time.sleep(2)
        console.clear()

#! /usr/bin/python3.6
import random


def game_help(minimum=0, maximum=100):

    print("""
                you have 5 chance to guess number in our mind that
                is between {min_}<number<{max_}.
    
          """.format(min_=minimum, max_=maximum))


def guess_number():
    maximum = 100
    minimum = 0
    game_help(minimum, maximum)
    random_number = random.randint(minimum, maximum)
    player_chance = 5

    while True:
        guessed = False
        your_guess = input("Remained Chance({chance})>".format(chance=player_chance)).lower().split()

        if not len(your_guess):
            continue

        if len(your_guess) > 1:
            print("Wrong input, please enter just one number in each round.")
            continue

        if not your_guess[0].isnumeric():
            print("Wrong input, what are you doing? please enter a number.")
            continue

        if not minimum < int(your_guess[0]) < maximum:
            guessed = False
            print("Wrong ,enter  number between %d and %d." % (minimum, maximum))

        else:
            guessed_number = int(your_guess[0])
            if guessed_number == random_number:
                guessed = True
                break
            if guessed_number < random_number:
                print("Wrong ,please enter a bigger number.")
            else:
                print("Wrong ,please enter a smaller number.")
        if not guessed:
            player_chance -= 1
            if player_chance == 0:
                guessed = False
                break
    if guessed:
        print("congratulation you guess our number {random_num} successfully."
              "".format(random_num=random_number))
    else:
        print("oh oh oh! you lose. our number is {random_num}.".format(random_num=random_number))


def main():
    answer = input("Are you ready to guess number in our mind?(press y to continue)\n>")

    if answer.lower() != "y":
        print("Come back as soon as possible.")
        exit(0)

    print("Let's Go.")

    guess_number()


if __name__ == "__main__":
    main()

import random


def clear():
    print("\n"*100)


def game():
    number = random.randint(1, 101)
    guess = 1
    print("You have to guess a number between 1 to 100.\nYou have a total of 9 guesses!")
    while(guess <= 9):
        guessed = int(input("Guess the number:\n"))
        if guessed > number:
            print("Your number is greater than the number to be guessed!\n")
            print(9 - guess, "number of guesses left")
            guess = guess + 1
            continue
        elif guessed < number:
            print("Your number is smaller than the number to be guessed!\n")
            print(9 - guess, "number of guesses left")
            guess = guess + 1
            continue
        else:
            print("Congratulations! You guessed the number!")
            print("You took", guess, "number of guesses to solve!")
            guess = guess + 1
            input("Press Enter to continuer")
            break

    if guess > 9:
        print("GAME OVER")
        input("Press Enter to continue")


if __name__ == '__main__':
    while True:
        clear()
        print("Press R to Start or Q to quit", end=" ")
        choice = input(": ")
        choice = choice.upper()
        if choice == 'Q':
            exit()
        elif choice == 'R':
            game()
        else:
            print("ERROR!!")

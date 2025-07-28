import random
import sys

# from art import logo

def random_num():
    return random.randint(1,100)

def cont():
    if input("Continue? 'y/n': ") =='y':
        guessing_game()
    else:
        print("See you next time!")
        sys.exit()


def guessing_game():
    print("\n" * 20)
    # print(logo)
    num = random_num()
    lives = 0
    print("Welcome to the guessing game! \nI'm thinking of a number between 1 and 100.")
    i = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if i == 'easy':
        lives = 10
    else:
        lives = 5
    while lives > 0:
        print(f"You have {lives} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess > int(num):
            print("Too high. \nGuess again.")
            lives -= 1
        elif guess < int(num):
            print("Too low. \nGuess again.")
            lives -= 1
        else:
            print("You guessed right!")
            cont()

    print("No more lives!")
    cont()
guessing_game()
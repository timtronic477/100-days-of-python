import random
from hangman_art import *
from hangman_words import *
#Step 1 



print(logo)
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')


word_length = len(chosen_word)

display = []
for i in range(word_length):
    display.append("_")
print(display)

lives = 6
game_over = False
wrong_guesses = []

while game_over == False:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You already guessed that, try something else")
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = guess
        
    if guess not in chosen_word:
        print (f"You guessed the letter {guess}, you lose a life")
        wrong_guesses.append(guess)
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lost")

    print(display)   
    if "_" not in display:
        game_over = True
        print("You win")           
        
    print(stages[lives]) 

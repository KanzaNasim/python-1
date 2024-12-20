# a take on the hangman game:)
import random
from hangman_hints import hint,word_list
from hangman_stages import stages,title


print(title[0])
print("*************************")
input("Press enter to continue...")
print("*************************")

word = random.choice(word_list).lower()
guess_list = ["_"] * len(word)

wrong_guesses = 6

while True:
    guess = input(f"Guess the letters (there are {len(word)} letters, write them one at a time): {''.join(guess_list)} ").lower()

    if guess in word:
        print("Nice guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guess_list[i] = guess
        print(f"It is one of the letters: {''.join(guess_list)}")
    else:
        print("Wrong guess!")
        print(stages[6 - wrong_guesses])
        print("*************************")
        print(f"You have {wrong_guesses} lives remaining.")
        print("*************************")
        print(hint[wrong_guesses % len(hint)])
        wrong_guesses -= 1

        if wrong_guesses == 0:
            print("*************************")
            print("You have 1 life remaining. I'll give you one more chance!")
            print("*************************")
            guess = input(f"Guess the letters (there are {len(word)} letters, write them one at a time): {''.join(guess_list)} ").lower()
            if guess in word:
                print("Nice guess!")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guess_list[i] = guess
                print(f"It is one of the letters: {''.join(guess_list)}")
            else:
                print("Wrong guess!")
                print(stages[6])
                print("*************************")
                print("Game over!")
                print(f"The word was: {word}")
                break

    if "".join(guess_list) == word:
        print("Yay, you did it!")
        y = input("Wanna play again? (y or n): ").lower()
        if y == 'y':
            word = random.choice(word_list).lower()
            guess_list = ["_"] * len(word)
            wrong_guesses = 6
        else:
            print("Okay, thanks for playing!")
            break


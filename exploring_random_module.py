# let's have a Toss at understanding randomness in python 
import random

a=random.randint(1,10)

def play_toss():
    if a>5:
        print("Heads")
    else:
        print("tails")

play_again=input("wanna toss? enter Y or N.....").lower()
while play_again == "y":
        play_toss()
        play_again=input("wanna toss again? enter Y or N.....").lower()
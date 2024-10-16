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



import random

# playing wih List:
Female = ["Ayla", "Emaan", "Hira", "Mahira", "Zoya"]

def get_random_number():
    i = random.randint(0, 4)
    return i

random_number = get_random_number()

print(Female[random_number])


import random

# playing wih List:
Female = ["Ayla", "Emaan", "Hira", "Mahira", "Zoya"]

# another way to do the above :
print(random.choice(Female))
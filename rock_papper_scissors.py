# playing rock,paper,scissors
import random
# Rock
rock= """Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors=""" Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Create a list containing the items
items = [rock, paper, scissors]



def go():
    print("let's play rock, paper scissors")
    print("")
    
      # Loop until a valid input is received
    while True:
        try:
            user_choice = int(input("Press 0 for rock, 1 for paper, and 2 for scissors: "))
            if user_choice in [0, 1, 2]:
                break
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
    
    print(f'''You chose:\n{items[user_choice]}''')
    print(f'''You chose:\n{items[user_choice]}''')
    my_pick=random.randint(0, 2)
    print("")
    print(f'''I pick:\n{items[my_pick]}''')
    
    # Determine the outcome
    if user_choice == my_pick:
        print("It's a tie!")
    elif (user_choice == 0 and my_pick == 2) or \
         (user_choice == 1 and my_pick == 0) or \
         (user_choice == 2 and my_pick == 1):
        print("You win!")
    else:
        print("I win!")
    
#calling the function
go()
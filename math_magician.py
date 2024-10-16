from helper_functions import *

math_magician= r""" 
Hi,
Iam MathMagician!

 
     1+1=2    /\
           \ c")
            ;-/\>
              ||    """

trick=input(f"{math_magician} wanna play a trick? y or n: ")


def math_magician (trick):
    if trick == "y":
        print("yay, let's play! Think of a number in your mind any number.")
        input("you can write it down here if you want to don't worry i won't look!, if done press enter....")
        
        print("Now imagine your friend has given you the same so add them both")
        input("if done press enter....")
        print(f"now add my number: {rnumber}")
        input("if done press enter....")
        print ("now give away the half of the total amount you have to the needy")
        input("if done press enter....")
        print("now return the money your friend gave you")
        input("if done press enter....")
        print(f"The number you have in your MIND is:{hnumber}")

MathMagic= math_magician (trick)
if trick == "y":
    print("Figure out how i did it ?")
else:
    print("too bad wish you had played!")
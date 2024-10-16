# function to generate random even number
import random

def generate_random_even_number():
    """Generates a random even number.

    Returns:
        int: A random even number.
    """

    while True:
        number = random.randint(0, 50) 
        if number % 2 == 0:
            return number
           
        
rnumber = generate_random_even_number()



# function to calculate half of a random even number
def calculate_half(rnumber):
    """Calculates half of a random even number.

    Args:
        random_even_number (int): The random even number.

    Returns:
        int: Half of the random even number.
    """

    return rnumber // 2


hnumber = calculate_half(rnumber)

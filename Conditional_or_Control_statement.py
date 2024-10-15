# practical example of conditional or control statement
print("It's a Calorie Intake Calculator")

weight = float(input("Input your weight here (kg): "))
height = float(input("Input your height here (m): "))

def calorie_calculator(weight, height):
    # Simple estimation for daily calorie needs
    calories = 10 * weight + 6.25 * (height * 100) - 5 * 25 + 5  # Assuming age 25 and male

    if calories < 2000:
        print("You need a low-calorie diet.")
    elif 2000 <= calories < 2500:
        print("You need a moderate-calorie diet.")
    else:
        print("You need a high-calorie diet.")

# Calling the function
calorie_calculator(weight, height)


print("welcome to burger house!")
size= input("what size burger do you want? S,M,L:")
pepperoni= input("do you want pepperoni in your burger? Y or N")
extra_cheese= input("do you want extra cheese? Y or N")


# Another example: Defining the function burger bill
def burger_bill(size, pepperoni, extra_cheese):
    if size == "L":
        result = 25
    elif size == "M":
        result = 20
    elif size == "S":
        result = 15
    else:
        print("you entered the wrong input")

    if pepperoni == "Y" and size == "L" or size == "M":
        result += 3
    elif pepperoni == "Y" and size == "S":
        result += 2
    if extra_cheese =="Y":
        result += 1

    return result 
    

bill = burger_bill (size,pepperoni, extra_cheese)
print(f"you final bill is: Rs{bill}")

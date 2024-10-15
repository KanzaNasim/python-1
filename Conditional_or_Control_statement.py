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
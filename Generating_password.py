import random

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
charac = ["!", '@', "#", "$", "%"]
capson = ["A", "B", "C", "D", "E"]
capsoff = ["a", "b", "c", "d", "e"]

Nnum = int(input("How many numbers do you want in your password? "))
Ncharac = int(input("How many special characters do you want in your password? "))
Ncapson = int(input("How many capital letters do you want in your password? "))
Ncapsoff = int(input("How many small letters do you want in your password? "))

def pass_generator(Nnum, Ncharac, Ncapson, Ncapsoff):
    password = []

    for _ in range(Nnum):
        password.append(str(random.choice(num)))

    for _ in range(Ncharac):
        password.append(random.choice(charac))

    for _ in range(Ncapson):
        password.append(random.choice(capson))

    for _ in range(Ncapsoff):
        password.append(random.choice(capsoff))

    print(password)
    random.shuffle(password)
    return ''.join(password)

generated_password = pass_generator(Nnum, Ncharac, Ncapson, Ncapsoff)
print("Generated Password:", generated_password)


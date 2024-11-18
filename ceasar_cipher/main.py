from ceasar_help import title

def caesar(message, shift, mode):
    if mode == "d":
        shift = -shift
    encrypted_message = ''
    for letter in message:
        if letter.isalpha():
            start = ord('a') if letter.islower() else ord('A')
            code = chr((ord(letter) - start + shift) % 26 + start)
            encrypted_message += code
        else:
            encrypted_message += letter
    return encrypted_message


restart = True

print(title)
print("")

while restart:
    intro = input("Press {e} to encrypt a message OR {d} to decrypt: ").lower()
    while intro not in ['e', 'd']:
        print("Invalid response. Press {e} to encrypt a message OR {d} to decrypt!")
        intro = input("Press {e} to encrypt a message OR {d} to decrypt: ").lower()

    message = input("Now, Enter your message: ")
    shift = int(input("Choose the shift number: "))

    result = caesar(message, shift, intro)
    print("The result is:", result)

    again = input("Press (y) to continue: ").lower()
    if again == "y":
        restart = True
    else:
        restart = False
        print("********The End********")
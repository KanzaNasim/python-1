# another way of writing ceasar cipher
def ceasar2(text,shift,direction):
    output_text=""
    if direction == "decode":
            shift *=-1
    for letter in text:
        if letter in alphabet:  
            shifted_position = alphabet.index(letter)+ shift
            shifted_position %= len(alphabet)# shifted_position %len(alphabet)
            output_text+=alphabet[shifted_position]
        else:
            output_text += letter  

    print(f"here is the {direction}d result is: {output_text}")

# calling the funtion 
print(title)

do_continue=True
while do_continue:
    direction = input("type encode to encrypt, type decode to decrypt:\n").lower()
    text=input("now enter your message !")
    shift= int(input("type the shift number:\n"))
    ceasar2(text,shift,direction)
    
    again=input("press 'yes' to continue\n").lower()
    if again !="yes":
        do_continue = False
        print("Thank you for your time :)")
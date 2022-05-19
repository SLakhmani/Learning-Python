# importing the logo from art.py
from art import logo

# defining the caesar cipher function
def caesar(text, shift, direction):
    
    final_text = ""
    
    # changing shift value depending on 'encode' or 'decode'
    if direction == "decode":
        shift *= -1
    
    # generating encrpyted / decrypted text
    for i in range(0, len(text)):
        if text[i].isalpha():
            letter_index = alphabet.index(text[i])
            if letter_index + shift > (len(alphabet) - 1):
                new_index = abs(len(alphabet) - letter_index - shift)
                final_text += alphabet[new_index]
            else:
                final_text += alphabet[letter_index + shift]
        else:
            final_text += text[i]

    return final_text

# defining function to reduce shift value for large inputs  
def reduce_shift(shift):
    shift_num = shift

    if shift_num % 26 == 0:
        shift_num = 0
    else:
        shift_num = shift_num % 26
        
    return shift_num

# alphabet character list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_program = 'y'

# continue running program while user selects 'y'
while continue_program == 'y':
    print(logo)
    # get user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if shift >= 26:
        shift = reduce_shift(shift)
    
    # print result and ask if user wants to continue
    result = caesar(text, shift, direction)
    print(f"\n{direction}d message: {result}\n")

    continue_program = input("Would you like to keep going? 'y' for yes / 'n' for no: ").lower()

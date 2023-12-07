import time
import os
from art import art
from morse_dic import morse_code_dict


# Convert text to morse code, and check for char not in the dic
def text_to_morse(message):
    morse_code = ''
    not_in_dict = [char for char in message.replace(" ", "") if char not in morse_code_dict.keys()]

    for char in message.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            print(f"\nWarning: {not_in_dict} doesn't exist.")
    return morse_code


# Convert morse code to text
def morse_to_text(morse_code):
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_code_dict.items():
            if morse == code:
                message += char
    return message


def play_morse_code(morse_code):
    for char in morse_code:
        if char == '/':
            time.sleep(3)
        else:
            morse_char = morse_code_dict.get(char)
            for dot_dash in morse_char:
                if dot_dash == ".":
                    os.system("afplay " + "dot.wav")
                elif dot_dash == '-':
                    os.system("afplay " + "dash.wav")
    return

is_on = True
print(art)
while is_on:
    print("Welcome to the Morse Converter!")
    print("1. Convert Text To Morse.\n2. Convert Morse to Text.\n3. Play Morse Code\n4. Exit\n")
    choice = input("Your choice: ")

    if choice == '1':
        message = input("Enter the message: ").upper()
        morse_msg = text_to_morse(message)
        print(f"\nMorse Code: {morse_msg}")

        play_it_or_not = input(f"\nPlay the Morse Code? (Y/N) ").upper()
        if play_it_or_not == 'Y':
            play_morse_code(message)
        else:
            time.sleep(3)

    elif choice == '2':
        invalid_input = False
        morse_msg = input("Enter the Morse message: ")
        for morse_sym in morse_msg:
            if morse_sym not in ['.', '-', ' ','/']:
                invalid_input = True
        if invalid_input:
            print("\nWarning: Invalid Input!!!")
        else:
            text_msg = morse_to_text(morse_msg)
            print(f"\n Message: {text_msg}")
        time.sleep(2)

    elif choice == '3':
        morse_or_text = input("PLay it from Morse(M) or Text(T)? (M/T) :").upper()
        if morse_or_text == 'M':
            morse = input("Enter the Morse Code: ").upper()
            if morse != "":
                play_morse_code(morse_to_text(morse))
        elif morse_or_text == 'T':
            text = input("Enter the Text: ").upper()
            if text != '':
                play_morse_code(text)

    elif choice == '4':
        is_on = False
        print("Exiting...")
        time.sleep(2)
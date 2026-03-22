ran_word = ["Birds","Dogs","Sun","Rain"]

import os
import random
def encrypter():
    def clear():
        os.system("cls")

    sentence = random.choice(ran_word).upper()
    shift = random.randint(-3,3)
    clear()
    encrypted_code = []
    for i in sentence:
        ascii_code = ord(i) + int(shift) 
        encrypted_code.append(str(ascii_code) + " ")

    for num in encrypted_code:
        print(num, end="")


        

import os
def clear():
    os.system("cls")

sentence = input('Enter a sentence: ')
clear()
shift = input('Give a encryption code(number): ')
clear()
encrypted_code = []
for i in sentence:
    ascii_code = ord(i) + int(shift)
    encrypted_code.append(ascii_code)




for num in encrypted_code:
    print(chr(num) + "", end="")

    
import os 
os.system('cls')

ascii_code = []
shifted_ascii =[]


sentence = input('Give an sentence: ')

for letter in sentence:
    ascii_code.append(ord(letter))


shift = int(input("Give an shift number:"))

for num in ascii_code:
    crypted = num + shift
    
    if crypted < 32:
        low_32 = (127 + (num - 32)) + shift
        shifted_ascii.append(low_32)

    elif crypted > 126:
        crypted = 33 - (127 - num)
        high_126 = crypted + shift
        shifted_ascii.append(high_126)

    else:
        shifted_ascii.append(crypted)
        


for i in shifted_ascii:
    print(chr(i), end="")

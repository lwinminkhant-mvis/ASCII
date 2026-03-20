import os
os.system('cls')


#Only work with 2 or more word in the sentence and with right shift

encrypted_ascii = []
decode =[]

x = 0
encrypted_text = input("waaaa: ")

for i in encrypted_text:
    encrypted_ascii.append(ord(i))



for num in encrypted_ascii:
    if 25 <= num <= 40:
        x = 32 - num

if x != 0:
    x = x * -1

for n in encrypted_ascii:
    decode.append(n - x)


word = ''

for a in decode:
    word += str(chr(a))

print(word)
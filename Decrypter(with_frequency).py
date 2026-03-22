import os
os.system('cls')

common_word = "esiarntolc"
sentence = input('Give an encrypted message: ')
total    = 0
real_senteece  = ''

for shift in range(0,95):
    temp_sentence = ''
    num = 0

    for letter in sentence:
        number = ord(letter) + shift

        if number > 126:
            number = (32 - (127 - ord(letter))) + shift
            temp_sentence += chr(number)
        else:
            temp_sentence += chr(number)

    for letter in temp_sentence:
        if letter in common_word:
            num += 1
        
    if num > total:
        total = num
        real_senteece = temp_sentence
        
print(f"The original sentence is : {real_senteece}")
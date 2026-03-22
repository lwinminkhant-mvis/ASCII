import os
os.system('cls')

common_word = "esiarntolc"
sentence = input('Give an encrypted message: ')
total    = 0
real_senteece  = ''
shifted = 0
for shift in range(1,95):
    temp_sentence = ''
    num = 0

    for letter in sentence:
        number = 32 + ((ord(letter) - 32 + shift) % 95)

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
        shifted = shift

shift_number = ord(sentence[:1]) - ord(real_senteece[:1])

print()
print("The top 5 most likely sentences:")
for i in range (5):
    top = ''
    for character in real_senteece:
        a = ord(character) + i 
        top += chr(a)
    print(i + 1 ,  top)
    print('------------------------')

print()
print(f"The shift number is      : {shift_number}")

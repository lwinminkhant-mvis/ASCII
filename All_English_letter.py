import os
os.system('cls')

english_letter_percentage = {
    'A': 8.17, 'a': 8.17,
    'B': 1.49, 'b': 1.49,
    'C': 2.78, 'c': 2.78,
    'D': 4.25, 'd': 4.25,
    'E': 12.70, 'e': 12.70,
    'F': 2.23, 'f': 2.23,
    'G': 2.02, 'g': 2.02,
    'H': 6.09, 'h': 6.09,
    'I': 6.97, 'i': 6.97,
    'J': 0.15, 'j': 0.15,
    'K': 0.77, 'k': 0.77,
    'L': 4.03, 'l': 4.03,
    'M': 2.41, 'm': 2.41,
    'N': 6.75, 'n': 6.75,
    'O': 7.51, 'o': 7.51,
    'P': 1.93, 'p': 1.93,
    'Q': 0.10, 'q': 0.10,
    'R': 5.99, 'r': 5.99,
    'S': 6.33, 's': 6.33,
    'T': 9.06, 't': 9.06,
    'U': 2.76, 'u': 2.76,
    'V': 0.98, 'v': 0.98,
    'W': 2.36, 'w': 2.36,
    'X': 0.15, 'x': 0.15,
    'Y': 1.97, 'y': 1.97,
    'Z': 0.07, 'z': 0.07
}
sentence = input('Give an encrypted message: ')
result = {}
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
        if letter in english_letter_percentage:
            num += english_letter_percentage[letter]
        
    result[num] = {"shift": shift, "sentence": temp_sentence}

result = dict(sorted(result.items(), reverse=True))


print("The top 5 most likely sentences:")
for i, (key, value) in (result.items()):
    if i < 5:
        print(f"{i + 1}. Points: {key}, Sentence: {value['sentence']}, Shift: {value['shift']}")
    else:
        break
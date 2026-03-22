import os
os.system('cls' )

def test_for_looping_encrypter():
    text = 'H #z'
    li = []
    shift = -8

    for i in text:
        a = ord(i) + shift
        if a < 32:
            y = (127 + ((a - shift) - 32)) + shift
            li.append(y)
        
        elif a > 126:
            l = 32 - (126-(a - shift))
            u = l + shift
            li.append(u)
        else:
            li.append(a)




    for x in li:
        print(chr(x), end="")

def simple_decoder():
    value = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    example = 'DCB'
    total = 0
    re_sentence = ''
    for i in example:
        if i in value:
            total = total + value[i]

    # print(total)

    for shift in range (1,4):
        letter = ""
        temp_num = 0

        for i in example:
            number = ord(i) + shift
            
            if number > 68:
                number = 65 - (69 - ord(i))
                number += shift
                letter += chr(number)

            else:
                letter += chr(number)
        
        for i in letter:
            if i in value:
                temp_num += value[i]

        if temp_num > total:
            total = temp_num
            re_sentence = letter
        
    print(total)
    print(letter)


def decoder_work():
    value = {"e":1,"s":1,"i":1,"a":1,"r":1,"n":1,"t":1,"o":1,"l":1,"c":1}

    sentence = input(": ")
    total = 0
    real_sentence = ''


    # for letter in sentence:
    #     if letter in value:
    #         total += value[letter]

    for shift in range(0,95):
        temp_sentence =''
        num = 0

        for let in sentence:
            number = ord(let) + shift
            if number > 126:
                number = 32 - (127 - ord(let))
                number += shift
                temp_sentence += chr(number)
            else:
                temp_sentence += chr(number)

        for letter in temp_sentence:
            if letter in value:
                num += value[letter]
        

        if num > total:
            total = num
            real_sentence = temp_sentence

    print(total)
    print(real_sentence)

decoder_work()
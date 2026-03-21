
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

test_for_looping_encrypter()
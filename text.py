text = 'H '
li = []
shift = -2
for i in text:
    a = ord(i) + shift
    if a < 32:
        y = 128 + shift
        li.append(y)
    elif a > 126:
        l = 32 - (a - 126)
        u = l + shift
        li.append(u)
    else:
        li.append(a)




for x in li:
    print(chr(x), end="")
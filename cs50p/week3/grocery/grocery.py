shoplist = {}

while True:
    try:
        add = input().upper()
        if add in shoplist:
            shoplist[add] += 1
        else:
            shoplist[add] = 1

    except EOFError:
        ordered = sorted(shoplist.items())
        for x in ordered:
            print(str(x[1]) + " " + x[0])
        break
    else:
        continue
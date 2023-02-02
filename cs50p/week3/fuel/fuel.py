gauge = input("Fraction: ")

def check(f):
    if "/" in f:
        x = f.split("/")
        y = x[0]
        z = x[1]
        if y.isnumeric() and z.isnumeric() and int(y) <= int(z):
            result = round((int(y) / int(z)) * 100)
            if result <= 1:
                print("E")
            if result >= 99:
                print("F")
            if 1 < result < 99:
                print(str(result)+ "%")
        else:
            guage = input("Fraction: ")
            check(guage)

    else:
        guage = input("Fraction: ")
        check(guage)

check(gauge)
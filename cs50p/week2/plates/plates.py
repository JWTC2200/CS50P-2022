from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and 2 <= len(s) <= 6 and s[0:2].isalpha() and zeronum(s) and midnum(s):
        return True

def zeronum(plate):
    for x in plate:
        if x.isnumeric():
            if x == "0":
                return False
            else:
                break
    return True

def midnum(plate):
    for i in range(len(plate)):
        if plate[i].isnumeric():
            for j in range(len(plate) - i):
                if plate[j + i].isalpha():
                    return False
    return True

main()

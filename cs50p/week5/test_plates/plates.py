def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    for x in s:
        if x.isnumeric():
            if x == "0":
                return False
            else:
                break
    for i in range(len(s)):
        if s[i].isnumeric():
            for j in range(len(s) - i):
                if s[j + i].isalpha():
                    return False
    return True

if __name__ == "__main__":
    main()

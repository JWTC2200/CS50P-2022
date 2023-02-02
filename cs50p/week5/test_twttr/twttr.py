

def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    for v in vowels:
        word = word.replace(v, "")
    return(word)

if __name__ == "__main__":
    main()
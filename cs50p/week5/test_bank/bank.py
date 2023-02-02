def main():
    greeting = input("Greeting: ")
    print("$" + str(value(greeting)))

def value(greeting):
    first = greeting.split()
    first_letter = first[0].lower().replace(",", "")
    if first_letter == "hello":
        return(0)
    elif first_letter[0] == "h":
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()

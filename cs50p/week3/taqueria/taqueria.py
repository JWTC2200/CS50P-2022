
menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


total = 0

while True:
    try:
        order = input("Item: ").lower()

        if order in menu:
            total += menu[order]
            print("Total: $" + str(total) +"0")
        else:
            continue

    except EOFError:
        print("\n")
        break
    else:
        continue
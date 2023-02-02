cost = 50
denom = ["25", "10", "5"]


def machine(cost):
    if cost > 0 :
        print("Amount Due: " + str(cost))
        coin = input("Insert Coin: ")
        if coin not in denom:
            machine(cost)
        else:
            cost = cost - int(coin)
            machine(cost)
    else:
        print("Change owed: " + str(cost).replace("-", ""))

machine(cost)



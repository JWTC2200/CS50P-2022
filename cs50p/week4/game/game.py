import random


def level():
    top = input("Level: ")
    if top.isnumeric() and int(top) >= 1:
        top = int(top)
        randnum = random.randint(1, top)
        guess(top, randnum)
    else:
        level()

def guess(level, randnum):
    g = input("Guess: ")
    if g.isnumeric() and int(g) >= 1:
        g = int(g)
        if g < randnum:
            print("Too small!")
            guess(level, randnum)
        if g > randnum:
            print("Too large!")
            guess(level, randnum)
        if g == randnum:
            print("Just right!")
    else:
        guess(level, randnum)

level()
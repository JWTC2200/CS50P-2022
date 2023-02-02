from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

arguments = len(sys.argv)

fontlist = figlet.getFonts()

# check correct number of arguments
if arguments != 1 and arguments != 3:
    sys.exit("Invalid usage")

if arguments == 1:
    text = input("Input: ")
    ranno = random.randint(0, 424)
    figlet.setFont(font=fontlist[ranno])
    print(figlet.renderText(text))

if arguments == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # if 3 arguments check for -f or --font
    if arg1 != "-f" and arg1 != "--font":
        sys.exit("Invalid usage")
    else:
        if arg2 not in fontlist:
            sys.exit("Invalid usage")
        figlet.setFont(font=arg2)
        text = input("Input: ")
        print(figlet.renderText(text))

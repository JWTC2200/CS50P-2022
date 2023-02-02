import sys

arguments = len(sys.argv)



def main():
    if arguments < 2:
        sys.exit("Too few command-line arguments")
    if arguments > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]
        if file[-1] == "y" and file[-2] == "p" and file[-3] == ".":
            print(linecheck(file))
        else:
            sys.exit("Not a Python file")


def linecheck(file):
    try:
        with open(file, "r") as check:
            lines = 0
            for row in check:
                strip = row.lstrip()
                if not strip.startswith("#") and not strip == "":
                    lines += 1

            return lines

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()




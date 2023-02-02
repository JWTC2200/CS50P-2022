import sys
from tabulate import tabulate
import csv


def main():
    arguments = len(sys.argv)
    if arguments < 2:
        sys.exit("Too few command-line arguments")
    if arguments > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]
        checkcsv = file[-4:]
        if checkcsv != ".csv":
            sys.exit("Not a CSV file")
        else:
            table = openfile(file)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

def openfile(file):
    try:
        with open(file, "r") as menu:
            table = []
            reader = csv.reader(menu)
            for row in reader:
                table.append(row)
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")







if __name__ == "__main__":
    main()
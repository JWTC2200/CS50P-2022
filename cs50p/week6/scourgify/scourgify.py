import sys
import csv
from os import path

def main():
    arguments = len(sys.argv)
    if arguments < 3:
        sys.exit("Too few command-line arguments")
    if arguments > 3:
        sys.exit("Too many command-line arguments")
    if not path.exists(sys.argv[1]):
        sys.exit("Could not read " + sys.argv[1])
    else:
        lis = []
        with open(sys.argv[1]) as before:
            beforefile = csv.DictReader(before)
            for row in beforefile:
                pre = row["name"].split(", ")
                first = pre[1]
                last = pre[0]
                house = row["house"]
                lis.append({"first": first, "last": last, "house": house})
        keys = ["first", "last", "house"]
        print(lis)
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, keys)
            writer.writeheader()
            writer.writerows(lis)

if __name__ == "__main__":
    main()
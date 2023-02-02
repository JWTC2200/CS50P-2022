import re
import sys


def main():
    print(count(input("Text: ").strip().lower()))


def count(s):
    if count := re.findall(r"(^|\W)(um)($|\W)", s, re.IGNORECASE):
        return len(count)
    else:
        return 0


if __name__ == "__main__":
    main()

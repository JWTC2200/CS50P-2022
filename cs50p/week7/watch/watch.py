import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"(src=)", s):
        if re.search(r"(youtube)", s):
            if match := re.search(r"(embed/)(.+?)\"", s):
                code = match.group(2)
                return f"https://youtu.be/{code}"
    else:
        return None

if __name__ == "__main__":
    main()

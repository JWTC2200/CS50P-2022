import re
import sys


def main():
    print(convert(input("Hours: ").strip().lower()))


def convert(s):
    try:
        if grp := re.search(r"^([0-9:]+) ([apm]+) to ([0-9:]+) ([apm]+)$", s):
            first = grp.group(1)
            second = grp.group(3)
            if ":" in first:
                if len(first) != 5:
                    first = f"0{first}"
                fSplit = first.split(":")
                if int(fSplit[1][0]) > 5:
                    raise ValueError
                if grp.group(2) == "pm":
                    fSplit[0] = str(int(fSplit[0]) + 12)
                if fSplit[0] == "12":
                    fSplit[0] = "00"
                if fSplit[0] == "24":
                    fSplit[0] = "12"
                first = f"{fSplit[0]}:{fSplit[1]}"
            elif ":" not in first:
                if grp.group(2) == "pm":
                    first = str(int(first) + 12)
                if len(first) != 2:
                    first = f"0{first}"
                if first == "12":
                    first = "00"
                if first == "24":
                    first = "12"
                first = f"{first}:00"
            if ":" in second:
                if len(second) != 5:
                    second = f"0{second}"
                sSplit = second.split(":")
                if int(sSplit[1][0]) > 5:
                    raise ValueError
                if grp.group(4) == "pm":
                    sSplit[0] = str(int(sSplit[0]) + 12)
                if sSplit[0] == "12":
                    sSplit[0] = "00"
                if sSplit[0] == "24":
                    sSplit[0] = "12"
                second = f"{sSplit[0]}:{sSplit[1]}"
            elif ":" not in second:
                if grp.group(4) == "pm":
                    second = str(int(second) + 12)
                if len(second) != 2:
                    second = f"0{second}"
                if second == "12":
                    second = "00"
                if second == "24":
                    second = "12"
                second = f"{second}:00"

            return f"{first} to {second}"

        else:
            raise ValueError

    except:
        raise ValueError

if __name__ == "__main__":
    main()

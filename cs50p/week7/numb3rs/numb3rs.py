import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if len(ip.split(".")) != 4:
        return False
    for i in ip.split("."):
        if not i.isdigit():
            return False
    else:
        check = "^(([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5])\\.){3}([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5]){1}$"
        if re.search(check, ip):
            return True
        else:
            return False

if __name__ == "__main__":
    main()

# I honestly had a lot of trouble with this one.
# The regex is something i googled as a solution and had to break down before I understood it.
# 000-199|200-249|250-255
# Originally I used in range(256) to check each part of the ip.split()
# After swapping over to the regex instead I noticed that it would still accept empty parts as valid such as ...
# added a bit to check each part of the split was a digit.
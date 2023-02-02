def main():
    time = input("What time is it?:")
    check = convert(time)

    if 7.0 <= check <= 8.0:
        print("breakfast time")

    if 12.0 <= check <= 13.0:
        print("lunch time")

    if 18.0 <= check <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    mins = int(minutes) / 60
    result = int(hours) + mins
    return result


if __name__ == "__main__":
    main()


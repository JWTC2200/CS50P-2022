def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        try:
            x = fraction.split("/")
            y = int(x[0])
            z = int(x[1])
            percentage = round((y / z) * 100)
            return percentage
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

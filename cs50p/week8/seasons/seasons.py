from datetime import date, time
import sys
import inflect

def main():
    inDate = input("Date of Birth: ")
    validDate = datecheck(inDate)
    minutes = conversion(validDate)
    print(text(minutes))

def datecheck(i):
    try:
        j = date.fromisoformat(i)
        return j
    except ValueError:
        sys.exit("Invalid date")

def conversion(d):
    today = date.today()
    difference = today - d
    minutes = difference.days * 24 * 60
    return minutes

def text(m):
    p = inflect.engine()
    txt = p.number_to_words(m, andword="")
    return (txt + " minutes").capitalize()


if __name__ == "__main__":
    main()

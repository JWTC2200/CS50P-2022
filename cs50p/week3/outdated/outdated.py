monthlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    enddate = checkdate()
    print(enddate)

def checkdate():
    date = input("Date: ")

    while True:
        try:
            if "/" in date:
                if " " in date:
                    date = date.replace(" ", "")
                date = date.split("/")
                year = int(date[2])
                month = int("0" + date[0])
                if int(month) > 12:
                    date = input("Date: ")
                day = int("0" + date[1])
                if int(day) > 31:
                    date = input("Date: ")
                enddate = f"{year:04}-{month:02}-{day:02}"
                return enddate

            elif "," in date:
                date = date.replace(",","").split(" ")
                year = date[2]
                if len(year) != 4:
                    date = input("Date: ")
                month = date[0].title()
                if month in monthlist:
                    month = monthlist.index(month) + 1
                day = int("0" + date[1])
                if int(day) > 31:
                    date = input("Date: ")
                enddate = f"{year}-{month:02}-{day:02}"
                return enddate

        except ValueError:
            date = input("Date: ")
        else:
            continue

main()

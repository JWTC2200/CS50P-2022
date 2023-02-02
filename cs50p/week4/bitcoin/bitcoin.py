import sys
import requests

r =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
    try:
        arg1 = float(arg1)
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        bitcoin = float(r.json()["bpi"]["USD"]["rate"].replace(",", ""))
        amount = bitcoin * float(arg1)
        print(f"${amount:,.4f}")

else:

    sys.exit("Missing command-line argument")
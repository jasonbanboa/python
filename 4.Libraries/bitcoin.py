import json
import requests
import sys


#
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
a = json.dumps(response.json(), indent=2)
o = response.json()
# print(o["bpi"]["USD"]["rate"]) also works ["rate_float"] returns float idk
o_bpi = o["bpi"]
o_currency = o_bpi["USD"]
o_rate = o_currency["rate"]
o_final = float(o_rate.replace(",", ""))


def main():
    try:
        checker()

    except requests.RequestException:
        sys.exit()


def isfloat(x):
    try:
        if float(x):
            return True

    except ValueError:
        sys.exit("Command-line argument is not a number")


def checker():
    if len(sys.argv) == 2 and isfloat(sys.argv[1]):
        amount = float(sys.argv[1]) * o_final
        print(f"${amount:,}")

    elif len(sys.argv) < 2:
        sys.exit("Missing command-line argument")




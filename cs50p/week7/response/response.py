from validator_collection import email


try:
    address = input("What's your email address? ").strip().lower()

    if email(address, allow_empty=False):
        print("Valid")

except:
    print("Invalid")
response  = input("Greeting:")

first = response.split()

check = first[0].lower().replace(",", "")

if check == "hello":
    print("$0")
elif check[0] == "h":
    print("$20")
else:
    print("$100")


print(check)
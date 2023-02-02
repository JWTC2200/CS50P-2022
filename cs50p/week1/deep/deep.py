reply = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

check = reply.lower().replace(" ", "")

answers = ["42", "forty-two", "fortytwo"]

if check in answers:
    print("Yes")
else:
    print("No")

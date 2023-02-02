request = input("Expression:")

split = request.split()
x = int(split[0])
y = split[1]
z = int(split[2])

if y == "+":
    answer = x + z

if y == "-":
    answer = x - z

if y == "*":
    answer = x * z

if y == "/":
    answer = x / z


print(float(answer))

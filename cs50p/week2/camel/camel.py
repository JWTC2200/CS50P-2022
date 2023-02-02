camel = input("camelCase: ")

print("snake_case: ", end="")

for snake in camel:
    if snake.isupper() == True:
        print("_" + snake.lower(), end="")
    else:
        print(snake, end="")

print("")



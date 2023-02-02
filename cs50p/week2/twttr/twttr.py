word = input("Input: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for w in word:
    if w in vowels:
        word = word.replace(w, "")

print(word)
#Q5
text = input("Enter sentence: ")
word = ""
short = 0
medium = 0
long = 0
for i in range(len(text) + 1):
    if i < len(text) and text[i] != " ":
        word += text[i]
    else:
        if word != "":
            n = len(word)
            print(word, n)
            if n <= 3:
                print("Short")
                short += 1
            elif n <= 6:
                print("Medium")
                medium += 1
            else:
                print("Long")
                long += 1
        word = ""
print("Short:", short)
print("Medium:", medium)
print("Long:", long)
# Q41. Count Words in a Sentence
s = input("Enter a sentence: ")
count = 0
in_word = False

for ch in s:
    if ch != " " and not in_word:
        count = count + 1
        in_word = True
    elif ch == " ":
        in_word = False

print(count)


# Q42. Replace All 'a' with 'e'
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch == "a":
        result = result + "e"
    else:
        result = result + ch

print(result)


# Q43. Check if String Contains a Character
s = input("Enter a string: ")
ch = input("Enter a character: ")
found = False

for c in s:
    if c == ch:
        found = True
        break

print(str(found).lower())


# Q44. Compare Two Strings (Exact Match)
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 == s2:
    print("true")
else:
    print("false")


# Q45. Count Digits in a String
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch >= "0" and ch <= "9":
        count = count + 1

print(count)


# Q46. Count Uppercase Letters
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch >= "A" and ch <= "Z":
        count = count + 1

print(count)


# Q47. Count Lowercase Letters
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch >= "a" and ch <= "z":
        count = count + 1

print(count)


# Q48. Remove All Vowels from a String
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.lower() not in "aeiou":
        result = result + ch

print(result)


# Q49. Remove All Digits from a String
s = input("Enter a string: ")
result = ""

for ch in s:
    if not (ch >= "0" and ch <= "9"):
        result = result + ch

print(result)


# Q50. Toggle Case of Each Character
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch >= "a" and ch <= "z":
        result = result + ch.upper()
    elif ch >= "A" and ch <= "Z":
        result = result + ch.lower()
    else:
        result = result + ch

print(result)

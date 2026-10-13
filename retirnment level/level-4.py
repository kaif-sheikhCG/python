# Q31. Length of String
s = input("Enter a string: ")
count = 0

for ch in s:
    count = count + 1

print(count)


# Q32. Print Each Character on New Line
s = input("Enter a string: ")

for ch in s:
    print(ch)


# Q33. Count Vowels
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count = count + 1

print(count)


# Q34. Count Consonants
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        count = count + 1

print(count)


# Q35. To Uppercase
s = input("Enter a string: ")
print(s.upper())


# Q36. To Lowercase
s = input("Enter a string: ")
print(s.lower())


# Q37. Reverse a String
s = input("Enter a string: ")
reverse = ""

for ch in s:
    reverse = ch + reverse

print(reverse)


# Q38. Palindrome String
s = input("Enter a string: ")
reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("true")
else:
    print("false")


# Q39. Count Occurrences of 'a'
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch == "a":
        count = count + 1

print(count)


# Q40. Remove All Spaces
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print(result)
# Q1. Stop Before Printing 5
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")


# Q2. Stop at the First Vowel
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)


# Q3. break in a while Loop
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2


# Q4. Stop at a Target Number
limit = int(input("Enter limit: "))

for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")
print()


# Q5. Find the First Matching Character
string = input("Enter string: ")
target = input("Enter target character: ")

for ch in string:
    print(ch, end=" ")
    if ch == target:
        break
print()


# Q6. Stop at a Negative Number
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for num in numbers:
    if num < 0:
        break
    print(num, end=" ")
print()


# Q7. break Only Exits the Inner Loop
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)


# Q8. Search a Word
sentence = input("Enter sentence: ")
target = input("Enter target word: ")

for word in sentence.split():
    if word == target:
        print("Found")
        break
else:
    print("Not found")


# Section B --- Practice Problems on continue

# Q9. Skip Number 4
for i in range(1, 7):
    if i == 4:
        continue
    print(i)


# Q10. Skip Vowels
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
print()


# Q11. continue in a while Loop
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


# Q12. Print Numbers That Are Not Multiples of 3
n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


# Q13. Remove a Chosen Character from Display
string = input("Enter string: ")
target = input("Enter character to remove: ")

for ch in string:
    if ch == target:
        continue
    print(ch, end="")
print()


# Q14. Print Only Passing Marks
marks = list(map(int, input("Enter marks separated by spaces: ").split()))

for mark in marks:
    if mark < 40:
        continue
    print(mark, end=" ")
print()


# Q15. continue Does Not Skip the Whole Loop
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)


# Q16. Fix the Infinite Loop
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)


# Q17. Count Non-Vowel Characters
word = input("Enter a word: ")
count = 0
for ch in word:
    if ch.lower() in "aeiou":
        continue
    count += 1
print(count)

# Section C --- Practice Problems on for-else

# Q18. Normal Completion
for i in range(1, 4):
    print(i)
else:
    print("Done")


# Q19. Completion After continue
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")


# Q20. Completion After break
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")


# Q21. Empty Iterable
for item in []:
    print("Inside")
else:
    print("Else block")


# Q22. Search for a Number
numbers = list(map(int, input("Enter list numbers: ").split()))
target = int(input("Enter target number: "))

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")


# Q23. Check Whether a Character Exists
string = input("Enter string: ")
target = input("Enter target character: ")

for ch in string:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")


# Q24. Find the First Divisor
n = int(input("Enter an integer greater than or equal to 2: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")


# Q25. Trace the else
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")


# Q26. Does else Run?

# Case A
for x in range(3):
    continue
else:
    print("A")

# Case B
for x in range(3):
    break
else:
    print("B")

# Case C
for x in range(0):
    print(x)
else:
    print("C")


# Q27. Find the First Repeated Character
string = input("Enter a string: ")

for i in range(len(string)):
    if string.count(string[i]) >= 2:
        print(string[i])
        break
else:
    print("No repeated character")


# Section D --- Practice Problems on pass

# Q28. pass Inside a Loop
for i in range(1, 4):
    if i == 2:
        pass
    print(i)


# Q29. Empty if Block
x = 10

if x > 5:
    pass

print("Finished")


# Q30. pass in a Loop Body
for letter in "cat":
    pass

print("Loop ended")


# Q31. Create a Placeholder for Future Work
for i in range(1, 6):
    if i % 2 == 0:
        pass
    print(i)


# Q32. Incomplete Menu Option
choice = int(input("Enter choice (1, 2, or 9): "))

if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    pass
else:
    print("Unknown option")

print("Program closed")


# Q33. Compare pass and continue

# Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)


# Q34. Complete the Skeleton
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Section E --- Mixed Challenge Questions

# Q35. Output Prediction
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")


# Q36. Search and Report
numbers = list(map(int, input("Enter list numbers: ").split()))
target = int(input("Enter target number: "))

for num in numbers:
    if num < 0:
        continue
    if num == target:
        print("Target found")
        break
else:
    print("Target not found")


# Q37. Skip, Stop, or Complete?
numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:
    if num == 0:
        continue
    if num == -1:
        break
    print(num)
else:
    print("All values processed")


# Q38. Understand Nested Loops
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")


# Q39. Find the First Number Divisible by Both 4 and 6
numbers = list(map(int, input("Enter numbers: ").split()))

for num in numbers:
    if num < 0:
        continue
    if num % 4 == 0 and num % 6 == 0:
        print("Found:", num)
        break
else:
    print("No matching number")


# Q40. Explain the Best Statement

print("1. Stop searching after finding a username: break")
print("2. Skip a blank string: continue")
print("3. Display Not found after an unsuccessful search: for-else")
print("4. Keep an unfinished function valid: pass")
print("5. Skip the current number: continue")
print("6. Stop when a sentinel value is entered: break")
print("7. Report all items checked without an early match: for-else")
print("8. Leave a conditional block temporarily empty: pass")
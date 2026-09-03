print("\n===== TASK 1: CREATE STRINGS =====")

name = "Kaif"
city = 'Kalol'
language = "Python"
message = 'I am learning Python strings'

print("Name:", name)
print("City:", city)
print("Language:", language)
print("Message:", message)


# ============================================================
# TASK 2 - EMPTY STRING
# ============================================================

print("\n===== TASK 2: EMPTY STRING =====")

empty_string = ""

print("String:", empty_string)
print("Length:", len(empty_string))
print("Data type:", type(empty_string))


# ============================================================
# TASK 3 - STRING INFORMATION
# ============================================================

print("\n===== TASK 3: STRING INFORMATION =====")

text = "Python Programming"

print("Complete string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])


# ============================================================
# PART 4 - INDEXING
# ============================================================

# TASK 4 - POSITIVE INDEXING

print("\n===== TASK 4: POSITIVE INDEXING =====")

text = "Programming"

print("First character:", text[0])
print("Second character:", text[1])
print("Fifth character:", text[4])
print("Last character:", text[len(text) - 1])


# TASK 5 - NEGATIVE INDEXING

print("\n===== TASK 5: NEGATIVE INDEXING =====")

print("Last character:", text[-1])
print("Second-last character:", text[-2])
print("Third-last character:", text[-3])
print("First character:", text[-len(text)])


# TASK 6 - INDEXING CHALLENGE

print("\n===== TASK 6: INDEXING CHALLENGE =====")

full_name = "Kaif Sheikh"

print("First character:", full_name[0])
print("Last character:", full_name[-1])

# First character of last name
last_name = "Sheikh"
print("First character of last name:", last_name[0])


# ============================================================
# PART 5 - SLICING
# ============================================================

# TASK 7 - BASIC SLICING

print("\n===== TASK 7: BASIC SLICING =====")

text = "Python Programming"

print("Python:", text[0:6])
print("Programming:", text[7:])
print("Complete:", text[:])
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])


# TASK 8 - SLICING WITH STEP

print("\n===== TASK 8: SLICING WITH STEP =====")

text = "ABCDEFGHIJKL"

print("Every second character:", text[::2])
print("Every third character:", text[::3])
print("Index 1 to 8 with step 2:", text[1:9:2])
print("Reverse:", text[::-1])


# TASK 9 - NEGATIVE SLICING

print("\n===== TASK 9: NEGATIVE SLICING =====")

text = "Python Programming"

print("Last 5 characters:", text[-5:])
print("Last 10 characters:", text[-10:])
print("Reverse:", text[::-1])


# TASK 10 - SLICING CHALLENGE

print("\n===== TASK 10: SLICING CHALLENGE =====")

text = "Programming"

print("First 3:", text[:3])
print("Last 3:", text[-3:])
print("Every second:", text[::2])
print("Reverse:", text[::-1])
print("Without first and last:", text[1:-1])


# ============================================================
# PART 6 - LENGTH
# ============================================================

# TASK 11

print("\n===== TASK 11: LENGTH =====")

word = "Python"
sentence = "Python is easy"
sentence_with_spaces = "  Python is easy  "

print("Word length:", len(word))
print("Sentence length:", len(sentence))
print("Sentence with spaces length:", len(sentence_with_spaces))


# TASK 12

print("\n===== TASK 12: LAST VALID INDEX =====")

text = "Python Programming"

last_index = len(text) - 1

print("Length:", len(text))
print("Last valid index:", last_index)
print("Last character:", text[last_index])


# ============================================================
# PART 7 - CONCATENATION
# ============================================================

# TASK 13

print("\n===== TASK 13: FULL NAME =====")

first_name = "Kaif"
last_name = "Sheikh"

full_name = first_name + " " + last_name

print("Full name:", full_name)


# TASK 14

print("\n===== TASK 14: SENTENCE CREATION =====")

name = "Kaif"
age = 18
city = "Kalol"
programming_language = "Python"

sentence = (
    "My name is " + name +
    ", I am " + str(age) +
    " years old, I live in " + city +
    " and I am learning " + programming_language + "."
)

print(sentence)


# TASK 15 - STRING AND INTEGER

print("\n===== TASK 15: STRING AND INTEGER =====")

age = 18

# Correct method using str()
print("Age: " + str(age))


# ============================================================
# PART 8 - STRING REPETITION
# ============================================================

# TASK 16

print("\n===== TASK 16: STRING REPETITION =====")

symbol = "*"

print("3 times:", symbol * 3)
print("5 times:", symbol * 5)
print("10 times:", symbol * 10)


# TASK 17

print("\n===== TASK 17: PATTERN =====")

print("*" * 10)


# ============================================================
# PART 9 - CASE CONVERSION
# ============================================================

# TASK 18

print("\n===== TASK 18: CASE CONVERSION =====")

text = "python programming language"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Swapcase:", text.swapcase())


# TASK 19

print("\n===== TASK 19: CASE-INSENSITIVE COMPARISON =====")

text1 = "Python"
text2 = "python"

print("Original comparison:", text1 == text2)

print("Lowercase comparison:", text1.lower() == text2.lower())


# ============================================================
# PART 10 - SEARCHING
# ============================================================

# TASK 20 - MEMBERSHIP

print("\n===== TASK 20: MEMBERSHIP =====")

text = "Python is a programming language"

print("Python:", "Python" in text)
print("programming:", "programming" in text)
print("Java:", "Java" in text)
print("language:", "language" in text)


# TASK 21 - FIND

print("\n===== TASK 21: FIND =====")

print("Python position:", text.find("Python"))
print("programming position:", text.find("programming"))
print("language position:", text.find("language"))
print("Java position:", text.find("Java"))


# TASK 22 - INDEX

print("\n===== TASK 22: INDEX =====")

print("Python position:", text.index("Python"))
print("programming position:", text.index("programming"))
print("language position:", text.index("language"))

# Do not use text.index("Java") here because it gives ValueError.


# TASK 23 - COUNT

print("\n===== TASK 23: COUNT =====")

text = "banana"

print("a count:", text.count("a"))
print("n count:", text.count("n"))
print("b count:", text.count("b"))


# TASK 24 - STARTS WITH AND ENDS WITH

print("\n===== TASK 24: STARTS WITH / ENDS WITH =====")

filename = "student_notes.pdf"

print("Starts with student:", filename.startswith("student"))
print("Ends with .pdf:", filename.endswith(".pdf"))
print("Ends with .txt:", filename.endswith(".txt"))


# ============================================================
# PART 11 - REPLACING
# ============================================================

# TASK 25

print("\n===== TASK 25: REPLACE A WORD =====")

text = "I am learning Java"

new_text = text.replace("Java", "Python")

print("Original:", text)
print("New:", new_text)


# TASK 26

print("\n===== TASK 26: MULTIPLE REPLACEMENTS =====")

text = "apple apple apple"

new_text = text.replace("apple", "mango")

print(new_text)


# TASK 27

print("\n===== TASK 27: LIMITED REPLACEMENT =====")

text = "apple apple apple"

new_text = text.replace("apple", "mango", 1)

print(new_text)


# TASK 28 - IMMUTABILITY

print("\n===== TASK 28: STRING IMMUTABILITY =====")

text = "Python"

text.upper()

print("After text.upper():", text)

text = text.upper()

print("After storing result:", text)


# ============================================================
# PART 12 - WHITESPACE
# ============================================================

# TASK 29

print("\n===== TASK 29: WHITESPACE =====")

text = "   Python Programming   "

print("Original:", repr(text))
print("strip():", repr(text.strip()))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))


# TASK 30 - USER INPUT

print("\n===== TASK 30: CLEAN USER INPUT =====")

user_name = input("Enter your name with possible extra spaces: ")

clean_name = user_name.strip()

print("Original:", repr(user_name))
print("Cleaned:", clean_name)


# ============================================================
# PART 13 - SPLIT AND JOIN
# ============================================================

# TASK 31

print("\n===== TASK 31: SPLIT =====")

text = "Python is easy to learn"

words = text.split()

print(words)


# TASK 32

print("\n===== TASK 32: SPLIT WITH SEPARATOR =====")

fruits = "apple,banana,mango,orange"

fruit_list = fruits.split(",")

print(fruit_list)


# TASK 33

print("\n===== TASK 33: JOIN =====")

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# TASK 34

print("\n===== TASK 34: JOIN WITH DIFFERENT SEPARATORS =====")

words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


# ============================================================
# PART 14 - STRING FORMATTING
# ============================================================

# TASK 35 - F STRING

print("\n===== TASK 35: F-STRING =====")

name = "Kaif"
age = 18
city = "Kalol"

sentence = f"My name is {name}, I am {age} years old and I live in {city}."

print(sentence)


# TASK 36 - ARITHMETIC INSIDE F STRING

print("\n===== TASK 36: ARITHMETIC IN F-STRING =====")

a = 10
b = 20

print(f"The sum is {a + b}")


# ============================================================
# PART 16 - PRACTICAL CHALLENGE
# TASK 38 - NAME PROCESSOR
# ============================================================

print("\n===== TASK 38: NAME PROCESSOR =====")

user_full_name = input("Enter your full name: ")

cleaned_name = user_full_name.strip()

print("Original input:", user_full_name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))

if len(cleaned_name) > 0:
    print("First character:", cleaned_name[0])
    print("Last character:", cleaned_name[-1])

character = input("Enter a character to search: ")

print(
    "Character exists:",
    character in cleaned_name
)


# ============================================================
# PART 17 - PRACTICAL CHALLENGE
# TASK 39 - SENTENCE ANALYZER
# ============================================================

print("\n===== TASK 39: SENTENCE ANALYZER =====")

sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))

words = sentence.split()

print("Number of words:", len(words))

if len(sentence) > 0:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())

print("Contains Python:", "Python" in sentence)

character = input("Enter a character to count: ")

print("Character count:", sentence.count(character))


# ============================================================
# PART 18 - FINAL CHALLENGE
# TASK 40 - STUDENT INFORMATION
# ============================================================

print("\n===== TASK 40: STUDENT INFORMATION =====")

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

# Create full name
full_name = first_name + " " + last_name

print("\n----- STUDENT DETAILS -----")

print("Full name:", full_name)
print("Title case:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Full name length:", len(full_name))

if len(full_name) > 0:
    print("First character:", full_name[0])
    print("Last character:", full_name[-1])

print("City:", city)
print("Course:", course)

print(f"Age: {age}")

print("Course contains Python:", "Python" in course)

# Replace Python with Java
new_course = course.replace("Python", "Java")

print("Course after replacement:", new_course)

print("Number of words in course:", len(course.split()))


# ============================================================
# END
# ============================================================

print("\n======================================")
print("ALL STRING PRACTICAL TASKS COMPLETED")
print("======================================")
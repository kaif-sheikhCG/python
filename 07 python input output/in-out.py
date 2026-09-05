# 1. Ask name and print it
name = input("1. Enter your name: ")
print(name)


# 2. Ask city
city = input("2. Enter your city: ")
print(f"Your city is {city}")


# 3. Name and age
name = input("3. Enter your name: ")
age = input("Enter your age: ")
print(name)
print(age)


# 4. Type returned by input()
value = input("4. Enter any value: ")
print(type(value))


# 5. Display type of input
value = input("5. Enter a value: ")
print(type(value))


# B. Multiple Inputs

# 6. First name and last name
first_name = input("6. Enter first name: ")
last_name = input("Enter last name: ")
print(first_name, last_name)


# 7. Name, city and college
name = input("7. Enter name: ")
city = input("Enter city: ")
college = input("Enter college: ")

print(name)
print(city)
print(college)


# 8. Two names using split()
name1, name2 = input("8. Enter two names: ").split()
print(name1)
print(name2)


# 9. Python Programming using split()
word1, word2 = input("9. Enter two words: ").split()
print(word1)
print(word2)


# 10. Three words using split()
word1, word2, word3 = input("10. Enter three words: ").split()

print(word1)
print(word2)
print(word3)


# C. Type Conversion

# 11. String to integer
value = int("25")
print("11.", value)


# 12. String to float
value = float("25.5")
print("12.", value)


# 13. Integer to string
value = str(100)
print("13.", value)


# 14. Integer input and type
age = int(input("14. Enter age: "))
print(type(age))


# 15. Float input and type
number = float(input("15. Enter a decimal number: "))
print(type(number))


# 16. String concatenation
a = input("16. Enter first number: ")
b = input("Enter second number: ")

print(a + b)


# 17. Numeric addition
a = int(input("17. Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)


# D. Formatted Output and f-Strings

# 18. Name and age
name = "Rahul"
age = 20

print(f"18. My name is {name} and I am {age} years old.")


# 19. Sum using f-string
a = 10
b = 20

print(f"19. The sum is {a + b}")


# 20. User name and age
name = input("20. Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


# 21. Price with two decimal places
price = float(input("21. Enter price: "))

print(f"Price: {price:.2f}")


# 22. Purpose of :.2f
print("22. :.2f displays a floating-point number with exactly two decimal places.")


# 23. Product information
product = input("23. Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")


# E. print() Formatting

# 24. Default print separator
print("24.", "A", "B", "C")


# 25. Custom separator
print("25.", "2026", "08", "19", sep="-")


# 26. Same line using end
print("26. Hello", end=" ")
print("World")


# F. Combined Practice

# 27. Two integers and sum
first = int(input("27. Enter first number: "))
second = int(input("Enter second number: "))

sum_value = first + second

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {sum_value}")


# 28. Price, quantity and total
price = float(input("28. Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")


# 29. Student information
name = input("29. Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")


# 30. Complete Student Information Program
name = input("30. Enter student name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")

print("\n--- Student Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")
# Part A — Intermediate Problems

# Problem 1: Valid Marks
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
    marks = int(input("Enter marks (0-100): "))
print("Accepted marks:", marks)


# Problem 2: Positive Integer
number = int(input("Enter a positive integer: "))
while number <= 0:
    print("Invalid number! Enter a number greater than 0.")
    number = int(input("Enter a positive integer: "))
print("Accepted number:", number)


# Problem 3: Age Validation
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Invalid age! Age must be between 0 and 120.")
    age = int(input("Enter your age: "))
print("Accepted age:", age)


# Problem 4: Menu Choice
choice = 0
while choice < 1 or choice > 4:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice < 1 or choice > 4:
        print("Invalid menu choice!")
print("Selected option:", choice)


# Problem 5: Password Length
password = input("Enter password: ").strip()
while len(password) < 8:
    print("Password must contain at least 8 characters.")
    password = input("Enter password: ").strip()
print("Password accepted!")


# Problem 6: Temperature Range
temperature = float(input("Enter temperature (-20 to 45): "))
while temperature < -20 or temperature > 45:
    print("Invalid temperature!")
    temperature = float(input("Enter temperature (-20 to 45): "))
print("Accepted temperature:", temperature)


# Problem 7: Withdrawal Validation
balance = 5000
amount = float(input("Enter withdrawal amount: "))
while amount <= 0 or amount > balance:
    print("Invalid withdrawal amount!")
    amount = float(input("Enter withdrawal amount: "))
balance = balance - amount
print("Withdrawal successful!")
print("Remaining balance: ₹", balance)


# Problem 8: Username Validation
username = input("Enter username: ").strip()
while len(username) < 5 or " " in username:
    print("Username must have at least 5 characters and no internal spaces.")
    username = input("Enter username: ").strip()
print("Accepted username:", username)


# Problem 9: Divisible Number
number = int(input("Enter a positive integer divisible by 3 and 5: "))
while number <= 0 or number % 3 != 0 or number % 5 != 0:
    print("Invalid number!")
    number = int(input("Enter a positive integer divisible by 3 and 5: "))
print("Accepted number:", number)


# Problem 10: Limited PIN Attempts
secret_pin = 2468
attempts = 0
while attempts < 3:
    pin = int(input("Enter PIN: "))
    attempts = attempts + 1
    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN!")
if attempts == 3 and pin != secret_pin:
    print("Access denied!")


# Problem 11: Number Within a Range
number = int(input("Enter an integer (10-50): "))
while number < 10 or number > 50:
    print("Invalid number!")
    number = int(input("Enter an integer (10-50): "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Problem 12: Deposit Validation
balance = 2000
amount = float(input("Enter deposit amount: "))
while amount <= 0:
    print("Deposit must be greater than zero!")
    amount = float(input("Enter deposit amount: "))
balance = balance + amount
print("Deposit successful!")
print("New balance: ₹", balance)


# Part B — Challenging Problems

# Problem 13: Integer Between 1 and 100
number = int(input("Enter an integer (1-100): "))
while number < 1 or number > 100:
    print("Invalid number!")
    number = int(input("Enter an integer (1-100): "))
print("Accepted number:", number)


# Problem 14: Marks and Result
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter marks (0-100): "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# Problem 15: Username and Password Validation
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
while len(username) < 5 or " " in username or len(password) < 8:
    print("Invalid username or password!")
    print("Username needs at least 5 characters and no internal spaces.")
    print("Password needs at least 8 characters.")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
print("Username and password accepted!")


# Problem 16: Calculator Input Validation
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator!")
    operator = input("Enter operator (+, -, *, /): ")

num2 = float(input("Enter second number: "))
while operator == "/" and num2 == 0:
    print("Division by zero is not allowed!")
    num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)


# Problem 17: Banking Menu
balance = 10000
choice = 0

while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        while amount <= 0:
            print("Deposit must be greater than zero!")
            amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        while amount <= 0 or amount > balance:
            print("Invalid withdrawal amount!")
            amount = float(input("Enter withdrawal amount: "))
        balance = balance - amount
        print("Withdrawal successful!")
        print("New balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using the banking system!")

    else:
        print("Invalid menu choice!")


# Problem 18: Validate Month and Day
month = int(input("Enter month (1-12): "))
while month < 1 or month > 12:
    print("Invalid month!")
    month = int(input("Enter month (1-12): "))

day = int(input("Enter day (1-31): "))
while day < 1 or day > 31:
    print("Invalid day!")
    day = int(input("Enter day (1-31): "))

print("Accepted month:", month)
print("Accepted day:", day)


# Problem 19: Product Quantity and Price
quantity = int(input("Enter product quantity: "))
while quantity <= 0:
    print("Quantity must be a positive integer!")
    quantity = int(input("Enter product quantity: "))

price = float(input("Enter unit price: "))
while price <= 0:
    print("Unit price must be greater than zero!")
    price = float(input("Enter unit price: "))

total = quantity * price
print("Total cost: ₹", total)


# Problem 20: Safe Average Calculator
count = int(input("How many numbers do you want to enter (1-20)? "))
while count < 1 or count > 20:
    print("Count must be between 1 and 20!")
    count = int(input("How many numbers do you want to enter (1-20)? "))

total = 0
for i in range(1, count + 1):
    number = float(input("Enter number " + str(i) + ": "))
    total = total + number

average = total / count
print("Average:", average)


# Problem 21: Stronger Password Rules
password = input("Enter a strong password: ")

while True:
    has_upper = False
    has_lower = False
    has_digit = False
    has_space = False

    for character in password:
        if character.isupper():
            has_upper = True
        if character.islower():
            has_lower = True
        if character.isdigit():
            has_digit = True
        if character.isspace():
            has_space = True

    valid = True

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        valid = False
    if not has_upper:
        print("Password must contain an uppercase letter.")
        valid = False
    if not has_lower:
        print("Password must contain a lowercase letter.")
        valid = False
    if not has_digit:
        print("Password must contain a digit.")
        valid = False
    if has_space:
        print("Password must not contain whitespace.")
        valid = False

    if valid:
        break

    password = input("Enter a strong password again: ")

print("Strong password accepted!")


# Problem 22: Input Validation Without break
number = int(input("Enter an integer (1-10): "))
while number < 1 or number > 10:
    print("Invalid number!")
    number = int(input("Enter an integer (1-10): "))
print("Accepted number:", number)


# Problem 23: Three Valid Scores
score1 = int(input("Enter score 1 (0-100): "))
while score1 < 0 or score1 > 100:
    print("Invalid score!")
    score1 = int(input("Enter score 1 (0-100): "))

score2 = int(input("Enter score 2 (0-100): "))
while score2 < 0 or score2 > 100:
    print("Invalid score!")
    score2 = int(input("Enter score 2 (0-100): "))

score3 = int(input("Enter score 3 (0-100): "))
while score3 < 0 or score3 > 100:
    print("Invalid score!")
    score3 = int(input("Enter score 3 (0-100): "))

total = score1 + score2 + score3
average = total / 3

print("Total score:", total)
print("Average score:", average)


# Problem 24: ATM Withdrawal With Denomination Rules
balance = 10000
amount = int(input("Enter withdrawal amount (multiple of ₹100): "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount! Enter a positive amount within balance and in multiples of ₹100.")
    amount = int(input("Enter withdrawal amount (multiple of ₹100): "))

balance = balance - amount
print("Withdrawn amount: ₹", amount)
print("Remaining balance: ₹", balance)

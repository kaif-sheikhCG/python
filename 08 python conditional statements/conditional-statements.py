```python
# 1
number = float(input("Enter a number: "))

if number > 10:
    print("Greater than 10")


# 2
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")


# 3
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")


# 4
marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Pass")


# 5
number = float(input("Enter a number: "))

if number == 0:
    print("Zero")


# 6
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
else:
    print("Not positive")


# 7
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 8
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 9
marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 10
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if first > second:
    print("First number is greater")
elif second > first:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# 11
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")


# 12
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 13
day = int(input("Enter day number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")


# 14
marks = float(input("Enter your marks: "))

if marks >= 75:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# 15
number = int(input("Enter a number: "))

if number == 1:
    print("One")
elif number == 2:
    print("Two")
elif number == 3:
    print("Three")
else:
    print("Other number")


# 16
age = int(input("Enter your age: "))

if age >= 18:
    if age <= 60:
        print("Age is between 18 and 60")
    else:
        print("Age is above 60")
else:
    print("Age is below 18")


# 17
marks = float(input("Enter your marks: "))

if marks >= 40:
    if marks >= 75:
        print("Passed with good marks")
    else:
        print("Passed")
else:
    print("Failed")


# 18
number = float(input("Enter a number: "))

if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    else:
        print("Positive and not greater than 100")
else:
    print("Not positive")


# 19
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")


# 20
number = float(input("Enter a number: "))

if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")


# 21
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not eligible")


# 22
number = float(input("Enter a number: "))

if number < 10 or number > 100:
    print("Special")
else:
    print("Normal")


# 23
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? yes/no: ")

if age >= 18 and has_id == "yes":
    print("Allowed")
else:
    print("Not allowed")


# 24
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if first > 10 and second > 10:
    print("Both numbers are greater than 10")
else:
    print("Both numbers are not greater than 10")


# 25
number = float(input("Enter a number: "))

if number < 0 or number > 100:
    print("Number is outside the range")
else:
    print("Number is inside the range")


# 26
is_closed = input("Is the shop closed? yes/no: ")

if not is_closed == "yes":
    print("Shop is open")
else:
    print("Shop is closed")


# 27
number = float(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Between 10 and 50")
else:
    print("Not between 10 and 50")


# 28
number = float(input("Enter a number: "))

if number < 10 or number > 50:
    print("Outside the range")
else:
    print("Inside the range")


# 29
is_student = input("Are you a student? yes/no: ")
has_id = input("Do you have an ID? yes/no: ")
has_ticket = input("Do you have a ticket? yes/no: ")

if is_student == "yes" and has_id == "yes" and has_ticket == "yes":
    print("Allowed")
else:
    print("Not allowed")


# 30
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
has_id = input("Do you have an ID? yes/no: ")

if age >= 18:
    if marks >= 40:
        if has_id == "yes":
            print("Eligible")
        else:
            print("Not eligible")
    else:
        print("Not eligible")
else:
    print("Not eligible")
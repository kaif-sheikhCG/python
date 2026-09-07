# 1. Basic if
number = int(input("Enter a number: "))

if number > 10:
    print("Greater than 10")


# 2. Basic if
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")


# 3. Basic if
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")


# 4. Basic if
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")


# 5. Basic if
number = int(input("Enter a number: "))

if number == 0:
    print("Zero")


# 6. If-else
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
else:
    print("Not positive")


# 7. If-else
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 8. If-else
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 9. If-else
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 10. If-else
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > second:
    print("First number is greater")
else:
    print("Second number is greater")


# 11. If-elif-else
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")


# 12. If-elif-else
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 13. If-elif-else
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
else:
    print("Other")


# 14. If-elif-else
marks = int(input("Enter marks: "))

if marks >= 75:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# 15. If-elif-else
number = int(input("Enter a number: "))

if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
else:
    print("Other")


# 16. Nested conditions
age = int(input("Enter your age: "))

if age >= 18:
    if age <= 60:
        print("Between 18 and 60")


# 17. Nested conditions
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")


# 18. Nested conditions
number = int(input("Enter a number: "))

if number > 0:
    if number > 100:
        print("Positive and greater than 100")
    else:
        print("Positive")


# 19. Nested conditions
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")


# 20. Nested conditions
number = int(input("Enter a number: "))

if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")


# 21. Multiple conditions
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")


# 22. Multiple conditions
number = int(input("Enter a number: "))

if number < 10 or number > 100:
    print("Special")


# 23. Multiple conditions
age = int(input("Enter your age: "))
has_id = input("Do you have ID? (True/False): ")

if age >= 18 and has_id == "True":
    print("Allowed")


# 24. Multiple conditions
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > 10 and second > 10:
    print("Both are greater than 10")


# 25. Multiple conditions
number = int(input("Enter a number: "))

if number < 0 or number > 100:
    print("Number is outside the range")


# 26. Logical operators
is_closed = False

if not is_closed:
    print("Open")


# 27. Logical operators
number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Between 10 and 50")


# 28. Logical operators
number = int(input("Enter a number: "))

if number < 10 or number > 50:
    print("Outside the range")


# 29. Logical operators
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")


# 30. Eligibility Checker
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have ID? (True/False): ")

if age >= 18 and marks >= 40 and has_id == "True":
    print("Eligible")
else:
    print("Not eligible")
#<----- Question 01 - Solve ----->
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#<----- Question 02 - Solve ----->
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")
elif num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")

#<----- Question 03 - Solve ----->
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Both are equal")

#<----- Question 04 - Solve ----->
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
else:
    print(num3)

#<----- Question 05 - Solve ----->
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(num1, "is the largest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")

#<----- Question 06 - Solve ----->
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible only by 5")
elif num % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")

#<----- Question 07 - Solve ----->
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
elif num % 3 == 0:
    print("Divisible only by 3")
elif num % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")

#<----- Question 08 - Solve ----->
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#<----- Question 09 - Solve ----->
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 40:
    print("E")
else:
    print("Fail")

#<----- Question 10 - Solve ----->
age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Can vote")
else:
    print("Cannot vote")

#<----- Question 11 - Solve ----->
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

#<----- Question 12 - Solve ----->
char = input("Enter a character: ")

if char >= "A" and char <= "Z":
    print("Uppercase alphabet")
elif char >= "a" and char <= "z":
    print("Lowercase alphabet")
elif char >= "0" and char <= "9":
    print("Digit")
else:
    print("Special character")

#<----- Question 13 - Solve ----->
char = input("Enter a character: ")

if char >= "A" and char <= "Z" or char >= "a" and char <= "z":
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print("Vowel")
    elif char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

#<----- Question 14 - Solve ----->
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No profit and no loss")

#<----- Question 15 - Solve ----->
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if cost_price <= 0:
    print("Invalid cost price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    percentage = profit / cost_price * 100
    print("Profit =", profit)
    print("Profit percentage =", percentage)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    percentage = loss / cost_price * 100
    print("Loss =", loss)
    print("Loss percentage =", percentage)
else:
    print("No profit and no loss")

#<----- Question 16 - Solve ----->
units = int(input("Enter units: "))
if units <= 100:
    bill = units*5
    print("Electricity bill =", bill)
elif units <= 200:
    bill = 100*5 + (units-100)*7
    print("Electricity bill =", bill)
else:
    bill = 100*5 + 100*7 + (units-200)*10
    print("Electricity bill =", bill)
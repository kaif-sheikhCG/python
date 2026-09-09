num =input("Enter a number: ")
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
 
 
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
 
 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
 
if a > b:
    print("Largest number is", a)
elif b > a:
    print("Largest number is", b)
else:
    print("Both are equal")
 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
 
if a <= b and a <= c:
    print("Smallest number is", a)
elif b <= a and b <= c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)
 
 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
 
if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")
 
 

num = int(input("Enter a number: "))
 
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible only by 5")
elif num % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")
 
 
num = int(input("Enter a number: "))
 
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
elif num % 3 == 0:
    print("Divisible only by 3")
elif num % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")
 

marks = float(input("Enter marks: "))
 
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
 
 

marks = float(input("Enter marks: "))
 
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
 
 
age = int(input("Enter age: "))
 
if age < 0 or age > 120:
    print("Invalid age")
elif age < 18:
    print("Cannot vote")
else:
    print("Can vote")
 
 

year = int(input("Enter a year: "))
 
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")
 
 
ch = input("Enter one character: ")
 
if ch >= 'A' and ch <= 'Z':
    print("Uppercase alphabet")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")
 

ch = input("Enter one character: ")
 
if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
       ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
 

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
 
 
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
 
if cost_price <= 0:
    print("Invalid cost price")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = profit / cost_price * 100
    print("Profit =", profit)
    print("Profit Percentage =", profit_percent)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percent = loss / cost_price * 100
    print("Loss =", loss)
    print("Loss Percentage =", loss_percent)
else:
    print("No profit and no loss")
 
 
units = float(input("Enter units consumed: "))
 
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
 
print("Electricity bill =", bill)
 
 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
 
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" and b == 0:
    print("Error: Division by zero is not allowed")
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
 
 
temp = float(input("Enter temperature in Celsius: "))
 
if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very Cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")
 
 
num = float(input("Enter a number: "))
 
if num < 0:
    print("Negative")
elif num <= 10:
    print("Number is between 0 and 10")
elif num <= 50:
    print("Number is between 11 and 50")
elif num <= 100:
    print("Number is between 51 and 100")
else:
    print("Number is above 100")
 
 
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
 
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

 
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
 
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
 
 

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
 
if amount <= 0:
    print("Withdrawal amount must be greater than 0")
elif amount % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < 500:
    print("Cannot withdraw: at least 500 must remain in the account")
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance - amount)
 
 
correct_username = "admin"
correct_password = "python123"
 
username = input("Enter username: ")
password = input("Enter password: ")
 
if username != correct_username:
    print("User not found")
elif password != correct_password:
    print("Wrong password")
else:
    print("Login successful")
 
 

amount = float(input("Enter purchase amount: "))
 
if amount < 500:
    discount_percent = 0
elif amount < 1000:
    discount_percent = 5
elif amount < 2000:
    discount_percent = 10
elif amount < 5000:
    discount_percent = 15
else:
    discount_percent = 20
 
discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount
 
print("Original amount:", amount)
print("Discount percentage:", discount_percent)
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)
 
 
# ---------------------------------------------------------------------------
# 25. Student Result System
# ---------------------------------------------------------------------------
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
 
if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("Invalid marks")
elif sub1 < 35 or sub2 < 35 or sub3 < 35:
    print("Fail")
else:
    average = (sub1 + sub2 + sub3) / 3
    if average >= 75:
        print("Average:", average, "- Distinction")
    elif average >= 60:
        print("Average:", average, "- First Class")
    elif average >= 50:
        print("Average:", average, "- Second Class")
    else:
        print("Average:", average, "- Pass")
 
 
# ---------------------------------------------------------------------------
# 26. Date Validator (no loops)
# ---------------------------------------------------------------------------
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
 
is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True
 
if month < 1 or month > 12:
    print("Invalid")
elif month == 1 or month == 3 or month == 5 or month == 7 or \
     month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        print("Valid")
    else:
        print("Invalid")
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        print("Valid")
    else:
        print("Invalid")
else:  # month == 2, February
    if is_leap:
        if day >= 1 and day <= 29:
            print("Valid")
        else:
            print("Invalid")
    else:
        if day >= 1 and day <= 28:
            print("Valid")
        else:
            print("Invalid")
 
 
# ---------------------------------------------------------------------------
# 27. Time Validator
# ---------------------------------------------------------------------------
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
 
if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and \
   seconds >= 0 and seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")
 
 
# ---------------------------------------------------------------------------
# 28. Youngest of Three People (no min(), lists, loops)
# ---------------------------------------------------------------------------
name1 = input("Enter name of person 1: ")
age1 = int(input("Enter age of person 1: "))
name2 = input("Enter name of person 2: ")
age2 = int(input("Enter age of person 2: "))
name3 = input("Enter name of person 3: ")
age3 = int(input("Enter age of person 3: "))
 
if age1 == age2 and age2 == age3:
    print("All three are of the same age")
elif age1 <= age2 and age1 <= age3:
    print(name1, "is the youngest")
elif age2 <= age1 and age2 <= age3:
    print(name2, "is the youngest")
else:
    print(name3, "is the youngest")
 
 
# ---------------------------------------------------------------------------
# 29. Second Largest of Three Numbers
# (no max(), min(), sort(), sorted(), lists, loops)
# ---------------------------------------------------------------------------
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
 
if (a > b and a < c) or (a < b and a > c):
    print("Second largest is", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second largest is", b)
else:
    print("Second largest is", c)
 
 
# ---------------------------------------------------------------------------
# 30. Complete Scholarship Decision
# ---------------------------------------------------------------------------
age = float(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))
 
age_ok = age >= 18 and age <= 25
marks_ok = marks >= 85
attendance_ok = attendance >= 75
income_ok = income <= 300000
 
if age_ok and marks_ok and attendance_ok and income_ok:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    if not age_ok:
        print("Reason: Age not between 18 and 25")
    if not marks_ok:
        print("Reason: Marks below 85")
    if not attendance_ok:
        print("Reason: Attendance below 75%")
    if not income_ok:
        print("Reason: Family income above 300000")
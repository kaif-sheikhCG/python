# PYTHON PROBLEM SOLVING
# IPO = Input, Processing, Output
# Algorithm = Clear and ordered steps to solve a problem
# Dry Run = Checking the logic using sample inputs


#  PROBLEM 1 
# Take two numbers and print their sum.

# IPO:
# Input: Two numbers
# Processing: Add them
# Output: Sum

# Algorithm:
# 1. Take two numbers
# 2. Add them
# 3. Print the sum

# Dry Run:
# 10, 20 => 10 + 20 = 30
# 50, 25 => 50 + 25 = 75

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


#  PROBLEM 2 
# Take a number and print whether it is even or odd.

# IPO:
# Input: Number
# Processing: Check number % 2
# Output: Even or Odd

# Algorithm:
# 1. Take a number
# 2. Check remainder after dividing by 2
# 3. If remainder is 0, print Even
# 4. Otherwise print Odd

# Dry Run:
# 10 -> 10 % 2 = 0 -> Even
# 7 -> 7 % 2 = 1 -> Odd

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#  PROBLEM 3 
# Take three numbers and print the largest.

# IPO:
# Input: Three numbers
# Processing: Compare them
# Output: Largest number

# Algorithm:
# 1. Take three numbers
# 2. Compare all three
# 3. Print the largest

# Dry Run:
# 10, 25, 15 -> Largest = 25
# 40, 20, 50 -> Largest = 50

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


#  PROBLEM 4 
# Check whether a person is eligible to vote.

# IPO:
# Input: Age
# Processing: Check age >= 18
# Output: Eligible or Not eligible

# Algorithm:
# 1. Take age
# 2. Check if age is 18 or more
# 3. Print the result

# Dry Run:
# 20 -> 20 >= 18 -> Eligible
# 16 -> 16 >= 18 -> Not eligible

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#  PROBLEM 5 
# Give 20% discount if price is 2000 or more.

# IPO:
# Input: Price
# Processing: Check price and calculate discount
# Output: Final price

# Algorithm:
# 1. Take price
# 2. If price >= 2000, calculate 20% discount
# 3. Subtract discount
# 4. Print final price

# Dry Run:
# 2500 -> Discount = 500 -> Final = 2000
# 1500 -> No discount -> Final = 1500

price = float(input("Enter price: "))

if price >= 2000:
    price = price - (price * 0.2)

print("Final price =", price)


#  PROBLEM 6 
# Calculate average of three marks and print Pass or Fail.

# IPO:
# Input: Three marks
# Processing: Calculate average and check average >= 40
# Output: Average and Pass/Fail

# Algorithm:
# 1. Take three marks
# 2. Calculate average
# 3. If average >= 40, print Pass
# 4. Otherwise print Fail

# Dry Run:
# 50, 60, 70 -> Average = 60 -> Pass
# 30, 35, 40 -> Average = 35 -> Fail

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

average = (m1 + m2 + m3) / 3

print("Average =", average)

if average >= 40:
    print("Pass")
else:
    print("Fail")


#  KEY LESSON 
# Understand -> IPO -> Algorithm -> Dry Run -> Code -> Test
# Do not start with code. Start with thinking.
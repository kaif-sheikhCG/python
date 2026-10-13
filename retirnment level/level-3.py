# Q21. Count Digits in a Number
n = int(input("Enter a number: "))
n = abs(n)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count = count + 1
        n = n // 10

print(count)


# Q22. Sum of Digits
n = abs(int(input("Enter a number: ")))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)


# Q23. Product of Digits
n = abs(int(input("Enter a number: ")))
product = 1

if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n // 10

print(product)


# Q24. Reverse a Number
n = int(input("Enter a number: "))
sign = 1

if n < 0:
    sign = -1
    n = abs(n)

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse * sign)


# Q25. Palindrome Number
n = int(input("Enter a number: "))
original = n
n = abs(n)
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original >= 0 and original == reverse:
    print("true")
else:
    print("false")


# Q26. Prime Number
n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

print(prime)


# Q27. All Primes from 1 to N
n = int(input("Enter N: "))

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")

print()


# Q28. First N Fibonacci Numbers
n = int(input("Enter N: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# Q29. GCD of Two Numbers
a = abs(int(input("Enter a: ")))
b = abs(int(input("Enter b: ")))
gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)


# Q30. LCM of Two Numbers
a = abs(int(input("Enter a: ")))
b = abs(int(input("Enter b: ")))

if a == 0 or b == 0:
    lcm = 0
else:
    if a > b:
        start = a
    else:
        start = b

    lcm = start

    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm = lcm + start

print(lcm)

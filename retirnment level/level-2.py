# Q11. Print 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()


# Q12. Print 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i, end=" ")
print()


# Q13. Even Numbers 1 to N
n = int(input("Enter N: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")
print()


# Q14. Odd Numbers 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")
print()


# Q15. Sum 1 to N
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print(total)


# Q16. Product 1 to N
n = int(input("Enter N: "))
product = 1

for i in range(1, n + 1):
    product = product * i

print(product)


# Q17. Multiplication Table of a Number
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n * i, end=" ")
print()


# Q18. Count Numbers Divisible by 3 (1 to N)
n = int(input("Enter N: "))
count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count = count + 1

print(count)


# Q19. Factorial (Iterative)
n = int(input("Enter N: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)


# Q20. First N Multiples of 7
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(7 * i, end=" ")
print()
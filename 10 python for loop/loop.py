#question 1
for i in range(1,6):
    print("Hello")

#question 2
for i in range(0,10):
    print(i,end=" ")

#question 3
for i in range(1,11):
    print(i,end=" ")

#question 4
for i in range(10,0,-1):
    print(i,end=" ")

#question 5
for i in range(5,50,5):
    print(i,end=" ")

#question 6
for i in range(2,21,2):
    print(i,end=" ")

#question 7
for i in range(1,20,2):
    print(i,end=" ")

#question 8
for i in range(3, 19, 3):
    print(i, end=" ")

#question 9
for i in range(20,1,-2):
    print(i,end=" ")

#question 10
n = int(input("Enter n:"))

for i in range(1,n+1):
    print(i,end=" ")

#question 11
n = int(input("Enter a number:"))

for i in range(1,n+1):
    if i%2 == 0:
        print(i,end=" ")

#question 12
n = int(input("Enter a number:"))

for i in range(1,n+1):
    if i%2 != 0:
        print(i,end=" ")

#question 13
n = int(input("Enter a number:"))

for i in range (1,1+n):
    if i%3 == 0:
        print(i,end=" ")

#question 14
n = int(input("Enter a number:"))

for i in range (1,n+1):
    if i%2==0 and i%3==0:
        print(i,end=" ")

#question 15
n = int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print("even numbers count :",count)

#question 16
n = int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum:",sum)

#question 17
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i

print("Sum:", sum)

#question 18
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        sum = sum + i

print("Sum:", sum)

#question 19
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#question 20
n = int(input("Enter n: "))

product = 1

for i in range(1, n + 1):
    product = product * i

print("Product:", product)

#question 21
text = input("Enter a string: ")

for i in text:
    print(i)

#question 22
string = input("Enter a string: ")

for i in string:
    print(i, end="")

#question 23
string = input("Enter a string: ")

count = 0

for i in string:
    count = count + 1

print("Number of characters:", count)

#question 24
s=input("enter string to kmow how many a in it:")
count=0
for i in s:
    if i=="a":
        count = count + 1
print("number of times a appeared:",count)

#question 25
string = input("Enter a string: ")

count = 0

for i in string:
    if i >= "A" and i <= "Z":
        count = count + 1

print("Uppercase letters:", count)

#question 26
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

#question 27
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

#question 28
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#question 29
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#question 30
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

#final challange
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
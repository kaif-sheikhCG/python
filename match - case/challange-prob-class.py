
# Challenge 1: Positive, Negative, and Zero

while True:
    num = int(input("Enter a number: "))

    if num < 0:
        continue

    if num == 0:
        break

    print(num)


# Challenge 2: Process a List

numbers = [12, 5, -4, 18, 0, 25, 30]

for num in numbers:
    if num < 0:
        continue

    if num == 0:
        break

    print(num)


# Challenge 3: Search for a Number in a List

numbers = [10, 20, 30, 40, 50]
print("select a number from : ",numbers)

search = int(input("Enter the number to search: "))

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")
# Q51. Print All Elements of an Array
arr = [1, 2, 3]

for i in range(len(arr)):
    print(arr[i], end=" ")
print()


# Q52. Sum of Array Elements
arr = [1, 2, 3]
total = 0

for i in range(len(arr)):
    total += arr[i]

print(total)


# Q53. Maximum in Array
arr = [3, 7, 2, 9]
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print(maximum)


# Q54. Minimum in Array
arr = [3, 7, 2, 9]
minimum = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]

print(minimum)


# Q55. Count Even Numbers in Array
arr = [1, 2, 3, 4, 5, 6]
count = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        count += 1

print(count)


# Q56. Count Odd Numbers in Array
arr = [1, 2, 3, 4, 5]
count = 0

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        count += 1

print(count)


# Q57. Print Only Positive Numbers
arr = [-1, 0, 5, 3, -2]

for i in range(len(arr)):
    if arr[i] > 0:
        print(arr[i], end=" ")
print()


# Q58. Print Only Negative Numbers
arr = [-1, 0, 5, 3, -2]

for i in range(len(arr)):
    if arr[i] < 0:
        print(arr[i], end=" ")
print()


# Q59. Print Elements Greater than 10
arr = [5, 12, 7, 20, 3]

for i in range(len(arr)):
    if arr[i] > 10:
        print(arr[i], end=" ")
print()


# Q60. Average of Array Elements
arr = [1, 2, 3, 4]
total = 0

for i in range(len(arr)):
    total += arr[i]

if len(arr) > 0:
    average = total / len(arr)
    print(average)
else:
    print(0)
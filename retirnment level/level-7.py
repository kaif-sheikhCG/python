
# Q61. Double Each Element
arr = [1, 2, 3]
new_arr = []

for i in range(len(arr)):
    new_arr.append(arr[i] * 2)

print(new_arr)


# Q62. Square Each Element
arr = [1, 2, 3]
new_arr = []

for i in range(len(arr)):
    new_arr.append(arr[i] * arr[i])

print(new_arr)


# Q63. Reverse Array into New Array
arr = [1, 2, 3]
new_arr = []

for i in range(len(arr) - 1, -1, -1):
    new_arr.append(arr[i])

print(new_arr)


# Q64. Copy Array
arr = [1, 2, 3]
new_arr = []

for i in range(len(arr)):
    new_arr.append(arr[i])

print(new_arr)


# Q65. Check if Array Contains a Value
arr = [1, 2, 3]
value = 2
found = False

for i in range(len(arr)):
    if arr[i] == value:
        found = True
        break

print(found)


# Q66. Find Index of a Value
arr = [10, 20, 30]
value = 20
index = -1

for i in range(len(arr)):
    if arr[i] == value:
        index = i
        break

print(index)


# Q67. Frequency of a Value
arr = [1, 2, 2, 3, 2]
value = 2
count = 0

for i in range(len(arr)):
    if arr[i] == value:
        count += 1

print(count)


# Q68. Check if Array is Sorted (Increasing)
arr = [1, 2, 2, 3]
sorted_arr = True

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        sorted_arr = False
        break

print(sorted_arr)


# Q69. Second Largest Element
arr = [10, 5, 8, 20]
largest = float("-inf")
second_largest = float("-inf")

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print(second_largest)


# Q70. Second Smallest Element
arr = [10, 5, 8, 20]
smallest = float("inf")
second_smallest = float("inf")

for i in range(len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print(second_smallest)

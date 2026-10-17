# # Level 1 - Nested Loop Basics

# # Q1. Number Pair Generator
# print("Q1 Output:")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# # Q2. Multiplication Pair
# print("\nQ2 Output:")
# n = int(input("Enter N for Q2: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i} x {j} = {i * j}")

# # Q3. Repeated Character Grid
# print("\nQ3 Output:")
# char = input("Enter a character for Q3: ")
# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))
# for i in range(rows):
#     for j in range(columns):
#         print(char, end="")
#     print()

# # Q4. Coordinate Grid
# print("\nQ4 Output:")
# rows = int(input("Enter rows for Q4: "))
# columns = int(input("Enter columns: "))
# for i in range(rows):
#     for j in range(columns):
#         print(f"({i},{j})", end=" ")
#     print()

# # Q5. Row Number Pattern
# print("\nQ5 Output:")
# n = int(input("Enter N for Q5: "))
# for i in range(1, n + 1):
#     for j in range(n):
#         print(i, end="")
#     print()

# # Q6. Column Number Pattern
# print("\nQ6 Output:")
# n = int(input("Enter N for Q6: "))
# for i in range(n):
#     for j in range(1, n + 1):
#         print(j, end="")
#     print()

# # Q7. Increasing Number Grid
# print("\nQ7 Output:")
# n = int(input("Enter N for Q7: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# # Q8. Decreasing Number Grid
# print("\nQ8 Output:")
# n = int(input("Enter N for Q8: "))
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# # Level 1 (continued)

# # Q9. Star Rectangle
# print("Q9 Output:")
# rows = int(input("Enter rows for Q9: "))
# columns = int(input("Enter columns for Q9: "))
# for i in range(rows):
#     for j in range(columns):
#         print("*", end="")
#     print()

# # Q10. Alternating 0 and 1
# print("\nQ10 Output:")
# n = int(input("Enter N for Q10: "))
# for i in range(n):
#     for j in range(n):
#         print(j % 2, end="")
#     print()

# # Level 2 - Conditions Inside Nested Loops

# # Q11. Even Number Grid
# print("\nQ11 Output:")
# rows = int(input("Enter rows for Q11: "))
# columns = int(input("Enter columns for Q11: "))
# for i in range(rows):
#     evens = [str(j) for j in range(1, columns + 1) if j % 2 == 0]
#     print(" ".join(evens))

# # Q12. Odd Number Grid
# print("\nQ12 Output:")
# n = int(input("Enter N for Q12: "))
# for i in range(n):
#     odds = [str(j) for j in range(1, n + 1) if j % 2 == 1]
#     print(" ".join(odds))

# # Q13. Even-Odd Classification
# print("\nQ13 Output:")
# for i in range(1, 5):
#     row = []
#     for j in range(1, 5):
#         row.append("E" if (i + j) % 2 == 0 else "O")
#     print(" ".join(row))

# # Q14. Equal Coordinate Detector
# print("\nQ14 Output:")
# n = int(input("Enter N for Q14: "))
# for i in range(1, n + 1):
#     row = []
#     for j in range(1, n + 1):
#         row.append("Same" if i == j else "Different")
#     print(" ".join(row))

# # Q15. Diagonal Values
# print("\nQ15 Output:")
# n = int(input("Enter N for Q15: "))
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append("1" if i == j else "0")
#     print(" ".join(row))

# # Q16. Number Divisibility Grid
# print("\nQ16 Output:")
# for i in range(1, 6):
#     row = []
#     for j in range(1, 6):
#         row.append("X" if i % j == 0 else "-")
#     print(" ".join(row))

# Q17. Multiples Detector
# For every i from 1 to N, print values j from 1 to N that are multiples of i.

# Test Case
# Input: N=4

# Expected Output:
# 1 2 3 4
# 2 4
# 3
# 4

# n=int(input("enter number: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%i==0:
#             print(j,end=" ")
#     print()

# Q18. Pair Sum Filter

# print("\nQ18 Output:")
# n = int(input("Enter N for Q18: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j > n:
#             print(i, j)

#q19
# # Print pairs and products only when the product is even
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         product = i * j
#         if product % 2 == 0:
#             print(i, j, product)

# Print SPECIAL for i==j, PAIR for i+j==N, otherwise NORMAL
# Priority: SPECIAL is checked first, so a cell on both the diagonal
# and the sum-N line (e.g. (2,2) when N=4) is labeled SPECIAL.

#q 20
# Print SPECIAL for i==j, PAIR for i+j==N, otherwise NORMAL
# Priority: SPECIAL is checked first, so a cell on both the diagonal
# and the sum-N line (e.g. (2,2) when N=4) is labeled SPECIAL.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print("SPECIAL", end=" ")
#         elif i + j == n:
#             print("PAIR", end=" ")
#         else:
#             print("NORMAL", end=" ")
#     print()

#Q21

# For every character, print it three times
s = input("Enter a string: ")
for ch in s:
    print(ch * 3)